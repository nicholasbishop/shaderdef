# pylint: disable=missing-docstring

import ast
from inspect import getsource

class _FindMethodVisitor(ast.NodeVisitor):
    # pylint: disable=invalid-name
    def __init__(self, method_name):
        super(_FindMethodVisitor, self).__init__()
        self._method_name = method_name
        self._method = None

    @property
    def method(self):
        return self._method

    def visit_FunctionDef(self, node):
        if node.name == self._method_name:
            self._method = node


def find_method_ast(cls, method_name):
    """Get the AST for a method in a class.

    A KeyError is raised if the method is not found.

    cls: class type (not a string)

    method_name: method to search for (string)
    """
    src = getsource(cls)
    node = ast.parse(src)

    finder = _FindMethodVisitor(method_name)
    finder.visit(node)

    if finder.method is None:
        raise KeyError('method not found', method_name)
    return finder.method
