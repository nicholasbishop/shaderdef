import ast
from shaderdef.ast_util import parse_source

from shaderdef.glsl_var import GlslVar
from shaderdef.glsl_types import vec4

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


def _declare_block(block_type, block_name, instance_name, members):
    # TODO
    assert len(members) != 0
    assert block_type in ('in', 'out', 'uniform')

    yield '{} {} {{'.format(block_type, block_name)

    for member in members:
        # TODO
        assert not member.name.startswith('gl_')
        yield '    ' + member.declare()

    yield '}} {};'.format(instance_name)


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
                # Ignore builtins
                if name.startswith('gl_'):
                    continue
                gtype = item.value.func.id
                interp = None
                if len(item.value.args) == 1:
                    interp = item.value.args[0].id
                yield GlslVar(name, gtype, interpolation=interp)

    @classmethod
    def _declare_block(cls, instance_name, block_type):
        members = list(cls._get_vars())
        if len(members) == 0:
            return []
        else:
            return list(_declare_block(block_type, cls.block_name(),
                                       instance_name, members))

    @classmethod
    def declare_input_block(cls, instance_name):
        return cls._declare_block(instance_name, 'in')

    @classmethod
    def declare_output_block(cls):
        instance_name = snake_case(cls.instance_name())
        return cls._declare_block(instance_name, 'out')

    @classmethod
    def block_name(cls):
        return cls.__name__

    @classmethod
    def instance_name(cls):
        return snake_case(cls.__name__)


class UniformBlock(ShaderInterface):
    @classmethod
    def declare_input_block(cls, instance_name):
        return cls._declare_block(instance_name, 'uniform')


class AttributeBlock(ShaderInterface):
    pass


# TODO, builtin
class GlGsIn(ShaderInterface):
    gl_position = vec4()
