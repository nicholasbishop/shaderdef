import ast
from shaderdef.ast_util import parse_source

from shaderdef.glsl_types import GlslVar


def snake_case(string):
    output = ''
    first = True
    for char in string:
        lower = char.lower()
        if char != lower:
            if first:
                first = False
            else:
                output += '_'
        output += lower
    return output


class ShaderInterface(object):
    def __init__(self, **kwargs):
        pass

    @classmethod
    def _get_vars(cls):
        # ast is used here instead of inspecting the attributes
        # directly because currently most of the types are just
        # aliases of GlslType rather than subclasses
        src = parse_source(cls)
        cls_node = src.body[0]
        for item in cls_node.body:
            if isinstance(item, ast.Assign):
                name = item.targets[0].id
                value = item.value
                yield name, value

    @classmethod
    def _get_gtype(cls, search_name):
        for name, value in cls._get_vars():
            gtype = value.func.id
            if gtype == search_name:
                gtype = value.args[0].func.id
                yield GlslVar(name, gtype)
            
    @classmethod
    def uniforms(cls):
        yield from cls._get_gtype('Uniform')

    @classmethod
    def attributes(cls):
        yield from cls._get_gtype('Attribute')

    @classmethod
    def glsl_declaration(cls, direction):
        # out VsOut {
#     vec3 vert_loc;
# 	vec3 vert_nor;
# 	vec4 vert_col;
# } vs_out;

        cls_name = cls.__name__

        yield '{} {} {{'.format(direction, cls_name)

        for name, value in cls._get_vars():
            # Don't declare builtins
            if name.startswith('gl_'):
                continue

            gtype = value.func.id
            yield '    ' + GlslVar(name, gtype).declare()

        yield '}} {};'.format(snake_case(cls_name))
