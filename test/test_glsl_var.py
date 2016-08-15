from unittest import TestCase

from shaderdef.glsl_var import GlslVar

class TestGlslVar(TestCase):
    def test_declare(self):
        self.assertEqual(GlslVar('x', 'vec3').declare(), 'vec3 x;')

    def test_declare_uniform(self):
        self.assertEqual(GlslVar('x', 'vec3').declare_uniform(),
                         'uniform vec3 x;')

    def test_declare_attribute(self):
        self.assertEqual(GlslVar('x', 'vec3').declare_attributes(),
                         'in vec3 x;')
