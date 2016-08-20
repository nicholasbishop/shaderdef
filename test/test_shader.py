from unittest import TestCase

from shaderdef.glsl_var import GlslVar
from shaderdef.glsl_types import vec4
from shaderdef.interface import ShaderInterface, UniformBlock
from shaderdef.shader import ShaderDef
from test.util import deindent


class MyMaterial(object):
    # pylint: disable=no-self-use

    class FsOut(ShaderInterface):
        color = vec4()

    def vert_shader(self):
        pass

    def geom_shader(self):
        pass

    def frag_shader(self) -> 'MyMaterial.FsOut':
        return MyMaterial.FsOut(color=vec4(1.0, 0.0, 0.0, 1.0))


class TestShader(TestCase):
    def test_simple(self):
        shader = ShaderDef(MyMaterial.vert_shader,
                           MyMaterial.geom_shader,
                           MyMaterial.frag_shader)
        shader.translate()
        self.assertEqual(deindent(shader.vert_shader),
                         '#version 330 core'
                         'void main() {}')
        self.assertEqual(deindent(shader.frag_shader),
                         '#version 330 core'
                         'out FsOut {'
                         'vec4 color;'
                         '} fs_out;'
                         'void main() {fs_out.color = vec4(1.0, 0.0, 0.0, 1.0);}')

    def test_get_uniforms(self):
        # pylint: disable=unused-argument
        class MyUniforms(UniformBlock):
            xyz = int()
        def func(unif: MyUniforms):
            pass
        shader = ShaderDef(func, func, func)
        self.assertEqual(list(shader.get_uniforms()),
                         [GlslVar('xyz', 'int')])

    def test_duplicate_uniform(self):
        # pylint: disable=unused-argument
        class MyUniforms1(UniformBlock):
            xyz = int()
        class MyUniforms2(UniformBlock):
            xyz = float()
        def func(unif1: MyUniforms1, unif2: MyUniforms2):
            pass
        shader = ShaderDef(func, func, func)
        with self.assertRaises(KeyError):
            shader.get_uniforms()
