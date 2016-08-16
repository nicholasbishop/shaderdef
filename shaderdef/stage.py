from ast import fix_missing_locations
from typing import Iterator, get_type_hints

from shaderdef.ast_util import (make_assign,
                                make_self_attr_load,
                                make_self_attr_store,
                                parse_source,
                                remove_function_parameters,
                                remove_function_return_type,
                                rename_function)
from shaderdef.attr_rename import rename_attributes
from shaderdef.find_deps import find_deps
from shaderdef.find_function import find_function
from shaderdef.lift_attributes import lift_attributes
from shaderdef.rewrite_output import rewrite_return_as_assignments
from shaderdef.unselfify import unselfify
from shaderdef.py_to_glsl import py_to_glsl


def make_prefix(name):
    parts = name.split('_')
    return ''.join(part[0] for part in parts) + '_'


def get_output_interface(func):
    return_type = get_type_hints(func).get('return')
    if return_type is None:
        return None
    # Unwrap iterators (used for geom shader output)
    origin = getattr(return_type, '__origin__', None)
    if origin is not None and origin == Iterator:
        return_type = return_type.__parameters__[0]
    return return_type


class Stage(object):
    def __init__(self, func):
        self.name = func.__name__
        root = parse_source(func)
        self.ast_root = find_function(root, self.name)
        self.input_prefix = ''
        self.output_prefix = make_prefix(self.name)
        self._glsl_source = None
        # TODO
        self._params = get_type_hints(func)
        self._params.pop('return', None)
        self._return_type = get_output_interface(func)

    def find_deps(self):
        return find_deps(self.ast_root)

    def provide_deps(self, next_stage):
        for dep in next_stage.find_deps().inputs:
            if dep not in self.find_deps().outputs:
                dst = make_self_attr_store(dep)
                src = make_self_attr_load(dep)
                assign = make_assign(dst, src)
                self.ast_root.body.append(assign)

        fix_missing_locations(self.ast_root)

    def required_uniforms(self, all_uniforms):
        for link in self.find_deps().inputs:
            unif = all_uniforms.get(link)
            if unif is not None:
                yield link, unif

    def load_names(self, external_links):
        names = {}
        for link in self.find_deps().inputs:
            if link not in external_links.uniforms:
                names[link] = self.input_prefix + link
        return names

    # TODO(nicholasbishop): de-dup
    def store_names(self, external_links):
        names = {}
        for link in self.find_deps().outputs:
            # Don't prefix uniforms, external outputs, or builtins
            if link not in external_links.uniforms and \
               link not in external_links.frag_outputs and \
               not link.startswith('gl_'):
                names[link] = self.output_prefix + link
        return names

    def _get_uniforms_or_attributes(self, func_name):
        used_names = set()
        for _, param_type in self._params.items():
            getter = getattr(param_type, func_name, None)

            # Branch will be taken for types like "Sequence[VsOut]"
            if getter is None:
                continue

            for var in getter():
                if var.name in used_names:
                    raise KeyError('duplicate attribute or uniform: ' +
                                   var.name)
                else:
                    yield var

    def uniforms(self):
        yield from self._get_uniforms_or_attributes('uniforms')

    def attributes(self):
        yield from self._get_uniforms_or_attributes('attributes')

    def declare_uniforms(self, lines):
        # TODO(nicholasbishop): limit to required_uniforms
        for var in self.uniforms():
            lines.append(var.declare_uniform())

    def declare_attributes(self, lines):
        # TODO(nicholasbishop): adjust index for type size
        for index, var in enumerate(self.attributes()):
            lines.append(var.declare_attribute(location=index))

    def declare_frag_outputs(self, lines, external_links):
        # TODO
        if self.name != 'frag_shader':
            return
        for link, fout in external_links.frag_outputs.items():
            lines.append(fout.glsl_decl(link))

    def declare_inputs(self, lines):
        # TODO
        pass
        # for pname, ptype in self.parameters:
        #     lines.append('in {} {};'.format(ptype, pname))

    def define_aux_functions(self, lines, library):
        # TODO
        for func_name in self.find_deps().calls:
            if func_name == 'emit_vertex':
                continue
            auxfunc = find_function(library, func_name)
            lines += py_to_glsl(auxfunc)

    def rename_gl_attributes(self, ast_root, external_links):
        return rename_attributes(
            ast_root,
            load_names=self.load_names(external_links),
            store_names=self.store_names(external_links))

    @staticmethod
    def rename_gl_builtins(ast_root):
        store_names = {
            'gl_position': 'gl_Position',
        }
        call_names = {
            'emit_vert': 'EmitVertex',
        }
        return rename_attributes(
            ast_root,
            store_names=store_names,
            call_names=call_names)

    @property
    def glsl(self):
        if self._glsl_source is None:
            raise ValueError('shader has not been translated yet')
        return self._glsl_source

    def translate(self):
        self._glsl_source = self.to_glsl()

    def to_glsl(self):
        lines = []
        lines.append('#version 330 core')

        self.declare_uniforms(lines)
        self.declare_attributes(lines)
        #self.declare_frag_outputs(lines, external_links)
        self.declare_inputs(lines)
        #self.define_aux_functions(lines, library)

        ast_root = self.ast_root

        # The main shader function must always be "void main()"
        rename_function(ast_root, 'main')
        remove_function_parameters(ast_root)
        remove_function_return_type(ast_root)

        #ast_root = self.rename_gl_attributes(ast_root, external_links)
        ast_root = self.rename_gl_builtins(ast_root)
        ast_root = rewrite_return_as_assignments(ast_root, self._return_type)
        ast_root = lift_attributes(ast_root, self._params.keys())

        if self._return_type is not None:
            lines += list(self._return_type.glsl_declaration('out'))

        ast_root = unselfify(ast_root)
        lines += py_to_glsl(ast_root)
        return '\n'.join(lines)
