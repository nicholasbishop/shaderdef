# pylint: disable=missing-docstring

import ast
from unittest import TestCase

from shaderdef.ast_util import parse_source, remove_function_parameters
from shaderdef.attr_rename import rename_attributes
from shaderdef.find_function import find_function
from test.util import AstTestCase


class SimpleClass(object):
    """Do-nothing class used in some of the tests."""
    def my_method(self):
        pass

    def method_with_params(self, thing: int):
        return self, thing


class TestFindFunction(TestCase):
    def setUp(self):
        self.root = parse_source(SimpleClass)

    def test_find_function(self):
        self.assertIsNot(find_function(self.root, 'my_method'), None)

    def test_function_not_found(self):
        with self.assertRaises(KeyError):
            find_function(self.root, 'bad_name')


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


class TestRemoveFunctionParameters(AstTestCase):
    def setUp(self):
        self.root = parse_source(SimpleClass)

    def test_remove_all_params(self):
        actual = find_function(self.root, 'method_with_params')
        remove_function_parameters(actual)

        root = ast.parse('def method_with_params(): return self, thing')
        expected = find_function(root, 'method_with_params')

        self.assertEqual(actual, expected)
