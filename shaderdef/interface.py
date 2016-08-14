import ast
from shaderdef.ast_util import parse_source

from shaderdef.glsl_types import GlslVar


class ShaderInterface(object):
    def __init__(self, **kwargs):
        pass

    @classmethod
    def _get_gtype(cls, search_name):
        # ast is used here instead of inspecting the attributes
        # directly because currently most of the types are just
        # aliases of GlslType rather than subclasses
        src = parse_source(cls)
        cls_node = src.body[0]
        for item in cls_node.body:
            if isinstance(item, ast.Assign):
                name = item.targets[0].id
                gtype = item.value.func.id
                if gtype == search_name:
                    gtype = item.value.args[0].func.id
                    yield GlslVar(name, gtype)
            
    @classmethod
    def uniforms(cls):
        yield from cls._get_gtype('Uniform')

    @classmethod
    def attributes(cls):
        yield from cls._get_gtype('Attribute')
