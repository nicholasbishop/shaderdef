# pylint: disable=missing-docstring

import ast

class _UnselfifyTransformer(ast.NodeTransformer):
    # pylint: disable=invalid-name,no-self-use
    def visit_Attribute(self, node):
        value = node.value
        if isinstance(value, ast.Name) and value.id == 'self':
            return ast.Name(id=node.attr, ctx=node.ctx)
        else:
            return node


def unselfify(root):
    """Modify an AST so that "self.some_attr" becomes "some_attr"."""
    return _UnselfifyTransformer().visit(root)
