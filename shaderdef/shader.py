from ast import fix_missing_locations
from shaderdef.ast_util import (make_assign,
                                make_self_attr_load,
                                make_self_attr_store,
                                rename_function)
from shaderdef.attr_rename import rename_attributes
from shaderdef.find_deps import find_deps
from shaderdef.find_method import find_method_ast
from shaderdef.glsl_types import Attribute, FragOutput, Uniform
from shaderdef.material import find_external_links
from shaderdef.py_to_glsl import py_to_glsl
from shaderdef.unselfify import unselfify


def make_prefix(name):
    parts = name.split('_')
    return ''.join(part[0] for part in parts) + '_'


class Stage(object):
    def __init__(self, obj, func_name):
        self.name = func_name
        self.ast_root = find_method_ast(obj, func_name)
        self.input_prefix = ''
        self.output_prefix = make_prefix(self.name)

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

    def to_glsl(self, external_links):
        lines = []
        for link, unif in self.required_uniforms(external_links.uniforms):
            lines.append(unif.glsl_decl(link))
        rename_function(self.ast_root, 'main')
        ast_root = rename_attributes(
            self.ast_root,
            load_names=self.load_names(external_links),
            store_names=self.store_names(external_links))
        ast_root = unselfify(ast_root)
        lines += py_to_glsl(ast_root)
        return '\n'.join(lines)


class ShaderDef(object):
    def __init__(self, material):
        self._material = material

        self._stages = []
        self._external_links = None
        self._vert_shader = None
        self._frag_shader = None

    def _create_stages(self):
        # TODO
        stage_names = ('vert_shader', 'frag_shader')
        for name in stage_names:
            yield Stage(self._material.__class__, name)

    def _thread_deps(self):
        """Link inputs and outputs between stages."""
        iter1 = reversed(self._stages)
        iter2 = reversed(self._stages)
        next(iter2)
        for stage, prev_stage in zip(iter1, iter2):
            stage.input_prefix = make_prefix(prev_stage.name)
            prev_stage.provide_deps(stage)

    def translate(self):
        self._stages = list(self._create_stages())
        self._external_links = find_external_links(self._material)

        self._thread_deps()

        # TODO
        self._vert_shader = self._stages[0].to_glsl(self._external_links)
        self._frag_shader = self._stages[1].to_glsl(self._external_links)

    @property
    def vert_shader(self):
        # TODO: declare inputs/outputs
        return self._vert_shader

    @property
    def frag_shader(self):
        # TODO: declare inputs/outputs
        return self._frag_shader
