from unittest import TestCase

from shaderdef.glsl_types import Uniform, vec3
from shaderdef.interface import ShaderInterface
from shaderdef.stage import Stage, make_prefix

class TestMakePrefix(TestCase):
    def test_vert_shader(self):
        self.assertEqual(make_prefix('vert_shader'), 'vs_')


class MockLinks(object):
    def __init__(self, uniforms):
        self.uniforms = uniforms


class TestStageUniforms(TestCase):
    class MyUnif(ShaderInterface):
        my_uniform = Uniform(vec3())

    def simple_stage(self, unif: MyUnif):
        pass

    def setUp(self):
        self.stage = Stage(self.simple_stage)

    def test_declare_uniforms(self):
        lines = []
        self.stage.declare_uniforms(lines)
        self.assertEqual(lines, ['uniform vec3 my_uniform;'])

    def test_to_glsl(self):
        text = self.stage.to_glsl()
        self.assertIn('uniform vec3 my_uniform;', text)
