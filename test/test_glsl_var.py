from unittest import TestCase

from shaderdef.glsl_var import GlslVar

class TestGlslVar(TestCase):
    def test_declare(self):
        var = GlslVar('x', 'vec3')
        self.assertEqual(var.declare(), 'vec3 x;')

    def test_declare_uniform(self):
        var = GlslVar('x', 'vec3')
        self.assertEqual(var.declare_uniform(), 'uniform vec3 x;')

    def test_declare_attribute(self):
        var = GlslVar('x', 'vec3')
        self.assertEqual(var.declare_attribute(), 'in vec3 x;')

    def test_declare_output(self):
        var = GlslVar('x', 'vec3')
        self.assertEqual(var.declare_output(), 'out vec3 x;')

    def test_declare_interpolation(self):
        var = GlslVar('x', 'vec3', interpolation='noperspective')
        self.assertEqual(var.declare_attribute(), 'noperspective in vec3 x;')
