# pylint: disable=missing-docstring

import ast
from unittest import TestCase

from shaderdef.attr_rename import rename_attributes
from shaderdef.find_deps import find_deps
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
    def my_method(self):
        pass


class TestFindMethod(TestCase):
    def test_find_method(self):
        self.assertIsNot(find_method_ast(SimpleClass, 'my_method'), None)

    def test_method_not_found(self):
        with self.assertRaises(KeyError):
            find_method_ast(SimpleClass, 'bad_name')


class TestAttrRename(AstTestCase):
    def test_load(self):
        root = rename_attributes(ast.parse('var = self.value1'),
                                 load_names={'value1': 'value2'})
        expected = ast.parse('var = self.value2')
        self.assertEqual(root, expected)

    def test_store(self):
        root = rename_attributes(ast.parse('self.var1 = value'),
                                 store_names={'var1': 'var2'})
        expected = ast.parse('self.var2 = value')
        self.assertEqual(root, expected)

    def test_load_and_store(self):
        root = rename_attributes(ast.parse('self.var1 = self.value1'),
                                 load_names={'value1': 'value2'},
                                 store_names={'var1': 'var2'})
        expected = ast.parse('self.var2 = self.value2')
        self.assertEqual(root, expected)

    def test_load_and_store_same_key(self):
        root = rename_attributes(ast.parse('self.foo1 = self.foo1'),
                                 load_names={'foo1': 'load'},
                                 store_names={'foo1': 'store'})
        expected = ast.parse('self.store = self.load')
        self.assertEqual(root, expected)

    def test_ignore_function_call(self):
        root = rename_attributes(ast.parse('self.myfunc(1)'),
                                 load_names={'myfunc': 'load'},
                                 store_names={'myfunc': 'store'})
        expected = ast.parse('self.myfunc(1)')
        self.assertEqual(root, expected)


class TestFindDeps(TestCase):
    def test_find_input(self):
        deps = find_deps(ast.parse('var = self.value'))
        self.assertEqual(deps.inputs, set(['value']))
        self.assertEqual(deps.outputs, set())

    def test_find_output(self):
        deps = find_deps(ast.parse('self.var = value'))
        self.assertEqual(deps.inputs, set())
        self.assertEqual(deps.outputs, set(['var']))

    def test_find_both(self):
        deps = find_deps(ast.parse('self.var = self.value'))
        self.assertEqual(deps.inputs, set(['value']))
        self.assertEqual(deps.outputs, set(['var']))
