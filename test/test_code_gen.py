import ast
from unittest import TestCase

from shaderdef.py_to_glsl import py_to_glsl


class TestPyToGlsl(TestCase):
    def assertCodeEqual(self, pycode, glslcode):
        root = ast.parse(pycode)
        code = ''.join(py_to_glsl(root))
        self.assertEqual(code, glslcode)

    def test_empty_function(self):
        self.assertCodeEqual('def myFunc(): pass', 'void myFunc() {}')

    def test_assign(self):
        self.assertCodeEqual('a = b', 'a = b;')

    def test_binop(self):
        self.assertCodeEqual('a - b * c / d', '(a - ((b * c) / d))')

    def test_subscript(self):
        self.assertCodeEqual('a[0]', 'a[0]')

    def test_unaryop(self):
        self.assertCodeEqual('-a', '-a')

    def test_augassign(self):
        self.assertCodeEqual('a += 1', 'a += 1;')

    def test_compare(self):
        self.assertCodeEqual('a < b', 'a < b')
