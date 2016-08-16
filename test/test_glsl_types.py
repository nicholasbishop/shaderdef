import ast
from unittest import TestCase

from shaderdef.glsl_types import ArraySpec


def get_node(string):
    node = ast.parse(string)
    return node.body[0].value


class TestArraySpec(TestCase):
    def test_no_type(self):
        node = get_node('Array4')
        self.assertIs(ArraySpec.from_ast_node(node), None)

    def test_invalid_type(self):
        node = get_node('Array4[1]')
        self.assertIs(ArraySpec.from_ast_node(node), None)

    def test_not_array(self):
        node = get_node('a[3]')
        self.assertIs(ArraySpec.from_ast_node(node), None)

    def test_no_length(self):
        node = get_node('Array[int]')
        self.assertIs(ArraySpec.from_ast_node(node), None)

    def test_valid(self):
        node = get_node('Array4[int]')
        self.assertEqual(ArraySpec.from_ast_node(node),
                         ArraySpec('int', 4))
