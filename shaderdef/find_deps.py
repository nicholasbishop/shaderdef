import ast

class FindDepsVisitor(ast.NodeVisitor):
    # pylint: disable=invalid-name
    def __init__(self):
        super(FindDepsVisitor, self).__init__()
        self.inputs = []
        self.outputs = []

    def visit_Attribute(self, node):
        if node.value.id == 'self':
            if isinstance(node.ctx, ast.Load):
                self.inputs.append(node.attr)
            elif isinstance(node.ctx, ast.Store):
                self.outputs.append(node.attr)


def find_deps(node):
    fdv = FindDepsVisitor()
    fdv.visit(node)
    return fdv
