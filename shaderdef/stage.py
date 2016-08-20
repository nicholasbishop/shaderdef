from typing import Iterator, Sequence, get_type_hints

from shaderdef.ast_util import (parse_source,
                                remove_function_parameters,
                                remove_function_return_type,
                                rename_function)
from shaderdef.find_function import find_function
from shaderdef.interface import (AttributeBlock, FragmentShaderOutputBlock,
                                 UniformBlock)
from shaderdef.lift_attributes import lift_attributes
from shaderdef.rename_ast_nodes import rename_gl_builtins
from shaderdef.rewrite_output import rewrite_return_as_assignments
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

    def declare_inputs(self, lines):
        for name, param_type in self._params.items():
            # TODO(nicholasbishop): dedup with return type
            origin = getattr(param_type, '__origin__', None)
            array = None
            if origin is not None and origin == Sequence:
                param_type = param_type.__parameters__[0]
                array = True
            lines += param_type.declare_input_block(instance_name=name,
                                                    array=array)

    def get_uniforms(self):
        for param_type in self._params.values():
            if issubclass(param_type, UniformBlock):
                yield from param_type.get_vars()

    @staticmethod
    def define_aux_functions(lines, library):
        # TODO(nicholasbishop): for now we don't attempt to check if
        # the function is actually used, just define them all
        for func in library:
            func_node = parse_source(func)
            lines += py_to_glsl(func_node)

    @property
    def glsl(self):
        if self._glsl_source is None:
            raise ValueError('shader has not been translated yet')
        return self._glsl_source

    def translate(self, library):
        self._glsl_source = self.to_glsl(library)

    def apply_decorators(self):
        decs = self.ast_root.decorator_list
        if len(decs) == 1 and decs[0].func.id == 'geom_shader_meta':
            kwargs = {}
            for keyword in decs[0].keywords:
                kwargs[keyword.arg] = keyword.value

            # TODO(nicholasbishop): validate inputs
            input_primitive = kwargs['input_primitive'].id
            output_primitive = kwargs['output_primitive'].id
            max_vertices = int(kwargs['max_vertices'].n)

            yield 'layout({}) in;'.format(input_primitive)
            yield 'layout({}, max_vertices = {}) out;'.format(output_primitive,
                                                              max_vertices)

    def attributes_to_lift(self):
        # Uniforms can use an interface block but for now we're not
        # doing that
        for param_name, param_type in self._params.items():
            if issubclass(param_type, UniformBlock):
                yield param_name

        # Attributes aren't allowed in an interface block
        for param_name, param_type in self._params.items():
            if issubclass(param_type, AttributeBlock):
                yield param_name

        # Same for fragment shader outputs. TODO(nicholasbishop): we
        # could also do this more directly during rewrite_return...
        if self._return_type is not None:
            if issubclass(self._return_type, FragmentShaderOutputBlock):
                yield self._return_type.instance_name()

    def to_glsl(self, library):
        lines = []
        lines.append('#version 330 core')

        lines += list(self.apply_decorators())
        self.declare_inputs(lines)
        self.define_aux_functions(lines, library)

        ast_root = self.ast_root

        # The main shader function must always be "void main()"
        rename_function(ast_root, 'main')
        remove_function_parameters(ast_root)
        remove_function_return_type(ast_root)

        ast_root = rewrite_return_as_assignments(ast_root, self._return_type)
        ast_root = lift_attributes(ast_root, set(self.attributes_to_lift()))
        ast_root = rename_gl_builtins(ast_root)

        if self._return_type is not None:
            lines += self._return_type.declare_output_block()

        lines += py_to_glsl(ast_root)
        return '\n'.join(lines)
