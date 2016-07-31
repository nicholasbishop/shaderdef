from unittest import TestCase

from shaderdef.glsl_types import Uniform, vec3

class TestGlslTypes(TestCase):
    def test_uniform_decl(self):
        self.assertEqual(Uniform(vec3).glsl_decl('x'), 'uniform vec3 x;')
