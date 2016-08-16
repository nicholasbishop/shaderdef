import ast
from unittest import TestCase

from shaderdef.py_to_glsl import py_to_glsl
from test.util import deindent

class TestPyToGlsl(TestCase):
    def assert_code_equal(self, pycode, glslcode):
        root = ast.parse(pycode)
        code = '\n'.join(py_to_glsl(root))
        self.assertEqual(deindent(code), glslcode)

    def test_empty_function(self):
        self.assert_code_equal('def myFunc(): pass', 'void myFunc() {}')

    def test_assign(self):
        self.assert_code_equal('a = b', 'a = b')

    def test_binop(self):
        self.assert_code_equal('a - b * c / d', '(a - ((b * c) / d))')

    def test_subscript(self):
        self.assert_code_equal('a[0]', 'a[0]')

    def test_unaryop(self):
        self.assert_code_equal('-a', '-a')

    def test_augassign(self):
        self.assert_code_equal('a += 1', 'a += 1')

    def test_compare(self):
        self.assert_code_equal('a < b', 'a < b')

    def test_if(self):
        self.assert_code_equal('if a: a = b', 'if (a) {a = b;}')

    def test_if_else(self):
        self.assert_code_equal('if a:\n return 1\n'
                               'else:\n return 2\n',
                               'if (a) {return 1;} else {return 2;}')

    def test_for(self):
        self.assert_code_equal('for i in range(3): a += 1',
                               'for (int i = 0; i < 3; i++) {a += 1;}')

    def test_nested_blocks(self):
        self.assert_code_equal('if a:\n if b: a = b',
                               'if (a) {if (b) {a = b;}}')

    def test_local_var(self):
        self.assert_code_equal('myvar = vec3(0, 0, 0)',
                               'vec3 myvar = vec3(0, 0, 0)')

    def test_local_array(self):
        self.assert_code_equal('arr = Array2[int]',
                               'int arr[2]')

    def test_array_param(self):
        self.assert_code_equal('def fn(arr: Array3[int]): pass',
                               'void fn(int arr[3]) {}')
