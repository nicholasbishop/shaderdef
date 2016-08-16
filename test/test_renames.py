import ast

from shaderdef.rename_ast_nodes import rename_ast_nodes
from test.util import AstTestCase


class TestRenames(AstTestCase):
    def test_rename_assign(self):
        root = ast.parse('a = 3')
        expected = ast.parse('b = 3')
        self.assertEqual(rename_ast_nodes(root, {'a': 'b'}), expected)

    def test_rename_attr_store(self):
        root = ast.parse('foo.a = 3')
        expected = ast.parse('foo.b = 3')
        self.assertEqual(rename_ast_nodes(root, {'a': 'b'}), expected)

    def test_rename_attr_load(self):
        root = ast.parse('foo = bar.a')
        expected = ast.parse('foo = bar.b')
        self.assertEqual(rename_ast_nodes(root, {'a': 'b'}), expected)
