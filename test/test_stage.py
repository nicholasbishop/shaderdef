from unittest import TestCase

from shaderdef.glsl_types import Uniform, vec3
from shaderdef.stage import Stage, make_prefix

class TestMakePrefix(TestCase):
    def test_vert_shader(self):
        self.assertEqual(make_prefix('vert_shader'), 'vs_')


class MockLinks(object):
    def __init__(self, uniforms):
        self.uniforms = uniforms


class TestStageUniforms(TestCase):
    def simple_stage(self):
        my_output = self.my_uniform

    def setUp(self):
        self.stage = Stage(TestStageUniforms, 'simple_stage')

    def test_required_uniforms(self):
        unifs = self.stage.required_uniforms({'my_uniform': Uniform(vec3)})
        self.assertEqual(list(unifs), [('my_uniform', Uniform(vec3))])

    def test_declare_uniforms(self):
        lines = []
        links = MockLinks({'my_uniform': Uniform(vec3)})
        self.stage.declare_uniforms(lines, links)
        self.assertEqual(lines, ['uniform vec3 my_uniform;'])
