import ast

class _FindDepsVisitor(ast.NodeVisitor):
    # pylint: disable=invalid-name
    def __init__(self):
        super(_FindDepsVisitor, self).__init__()
        self.inputs = set()
        self.outputs = set()
        self.calls = set()

    def __repr__(self):
        return 'Deps(inputs={}, outputs={}, calls={})'.format(self.inputs,
                                                              self.outputs,
                                                              self.calls)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Attribute):
            self.calls.add(node.func.attr)
            for arg in node.args:
                self.visit(arg)
        else:
            self.generic_visit(node)

    def visit_Attribute(self, node):
        value = node.value
        if isinstance(value, ast.Name) and value.id == 'self':
            if isinstance(node.ctx, ast.Load):
                self.inputs.add(node.attr)
            elif isinstance(node.ctx, ast.Store):
                self.outputs.add(node.attr)


def find_deps(node):
    """Find attributes of "self"."""
    fdv = _FindDepsVisitor()
    fdv.visit(node)
    return fdv
