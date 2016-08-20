from unittest import TestCase

from shaderdef.glsl_var import GlslVar
from shaderdef.interface import UniformBlock
from shaderdef.stage import Stage, make_prefix

class TestMakePrefix(TestCase):
    def test_vert_shader(self):
        self.assertEqual(make_prefix('vert_shader'), 'vs_')


class TestAuxFunction(TestCase):
    # pylint: disable=unused-argument
    def test_library(self):
        def simple_stage():
            pass

        def aux(self):
            pass

        stage = Stage(simple_stage)
        code = stage.to_glsl([aux])
        self.assertIn('void aux() {', code)


class TestUniforms(TestCase):
    def test_simple(self):
        # pylint: disable=unused-argument
        class MyUniforms(UniformBlock):
            xyz = int()
        def func(unif: MyUniforms):
            pass
        stage = Stage(func)
        self.assertEqual(list(stage.get_uniforms()), [
            GlslVar('xyz', 'int')
        ])

    def test_lift(self):
        # pylint: disable=unused-variable
        class MyUniforms(UniformBlock):
            xyz = int()
        def func(param: MyUniforms):
            abc = param.xyz
        stage = Stage(func)
        stage.translate([])
        self.assertIn('xyz', stage.glsl)
        self.assertNotIn('param', stage.glsl)
