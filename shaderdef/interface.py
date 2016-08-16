import ast
from shaderdef.ast_util import parse_source

from shaderdef.glsl_var import GlslVar


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


# https://www.opengl.org/wiki/Interface_Block_(GLSL)
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
        yield '{} {} {{'.format(direction, cls.block_name())

        for name, value in cls._get_vars():
            # Don't declare builtins
            if name.startswith('gl_'):
                continue

            gtype = value.func.id
            interp = None
            if len(value.args) == 1:
                interp = value.args[0].id
            yield '    ' + GlslVar(name, gtype, interp).declare()

        yield '}} {};'.format(cls.instance_name())

    @classmethod
    def block_name(cls):
        return cls.__name__

    @classmethod
    def instance_name(cls):
        return snake_case(cls.__name__)
