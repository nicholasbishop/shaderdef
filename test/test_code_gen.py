import ast
from unittest import TestCase

from shaderdef.py_to_glsl import py_to_glsl


class TestPyToGlsl(TestCase):
    def test_empty_function(self):
        root = ast.parse('def myFunc(): pass')
        code = ''.join(py_to_glsl(root))
        self.assertEqual(code, 'void myFunc() {}')

    def test_assign(self):
        root = ast.parse('a = b')
        code = ''.join(py_to_glsl(root))
        self.assertEqual(code, 'a = b;')

    def test_binop(self):
        root = ast.parse('a - b * c / d')
        code = ''.join(py_to_glsl(root))
        self.assertEqual(code, '(a - ((b * c) / d))')

    def test_subscript(self):
        root = ast.parse('a[0]')
        code = ''.join(py_to_glsl(root))
        self.assertEqual(code, 'a[0]')
