# pylint: disable=missing-docstring

import ast
from unittest import TestCase

from shaderdef.find_method import find_method_ast
from shaderdef.unselfify import unselfify


class AstTestCase(TestCase):
    def assertEqual(self, left, right, msg=None):
        if isinstance(left, ast.AST) and isinstance(right, ast.AST):
            left = ast.dump(left)
            right = ast.dump(right)
        return super(AstTestCase, self).assertEqual(left, right, msg)


class TestUnselfify(AstTestCase):
    def test_load(self):
        root = unselfify(ast.parse('var = self.value'))
        expected = ast.parse('var = value')
        self.assertEqual(root, expected)

    def test_store(self):
        root = unselfify(ast.parse('self.var = value'))
        expected = ast.parse('var = value')
        self.assertEqual(root, expected)

    def test_nonself(self):
        root = unselfify(ast.parse('foo.var = value'))
        expected = ast.parse('foo.var = value')
        self.assertEqual(root, expected)


class SimpleClass(object):
    def foo(self):
        pass


class TestFindMethod(AstTestCase):
    def test_find_method(self):
        self.assertIsNot(find_method_ast(SimpleClass, 'foo'), None)

    def test_method_not_found(self):
        with self.assertRaises(KeyError):
            find_method_ast(SimpleClass, 'bad_name')
