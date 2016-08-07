# pylint: disable=missing-docstring

import ast

class _FindFunctionVisitor(ast.NodeVisitor):
    # pylint: disable=invalid-name
    def __init__(self, function_name):
        super(_FindFunctionVisitor, self).__init__()
        self._function_name = function_name
        self._function = None

    @property
    def function(self):
        return self._function

    def visit_FunctionDef(self, node):
        if node.name == self._function_name:
            self._function = node


def find_function(root, function_name):
    """Search an AST for a function with the given name.

    A KeyError is raised if the function is not found.

    root: an AST node

    function_name: function to search for (string)
    """
    finder = _FindFunctionVisitor(function_name)
    finder.visit(root)

    if finder.function is None:
        raise KeyError('function not found', function_name)
    return finder.function
