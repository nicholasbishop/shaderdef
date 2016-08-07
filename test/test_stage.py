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
        # pylint: disable=no-member,unused-variable
        my_output = self.my_uniform

    def setUp(self):
        self.stage = Stage(TestStageUniforms, 'simple_stage')
        self.links = MockLinks({'my_uniform': Uniform(vec3)})

    def test_required_uniforms(self):
        unifs = self.stage.required_uniforms(self.links.uniforms)
        self.assertEqual(list(unifs), [('my_uniform', Uniform(vec3))])

    def test_declare_uniforms(self):
        lines = []
        self.stage.declare_uniforms(lines, self.links)
        self.assertEqual(lines, ['uniform vec3 my_uniform;'])

    def test_to_glsl(self):
        text = self.stage.to_glsl(self.links, library=None)
        self.assertIn('uniform vec3 my_uniform;', text)
