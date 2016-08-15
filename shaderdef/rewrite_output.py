import ast

def kwargs_as_assignments(call_node):
    """Yield Assign nodes from kwargs in a Call node."""
    if not isinstance(call_node, ast.Call):
        raise TypeError('node must be an ast.Call')

    if len(call_node.args) > 0:
        raise ValueError('positional args not allowed')

    for keyword in call_node.keywords:
        target = ast.Name(id=keyword.arg, ctx=ast.Load())
        yield ast.Assign(targets=[target], value=keyword.value)


class _RewriteReturn(ast.NodeTransformer):
    def visit_Return(self, node):
        return list(kwargs_as_assignments(node.value))


def rewrite_return_as_assignments(func_node):
    """Modify FunctionDef node to directly assign instead of return."""
    func_node = _RewriteReturn().visit(func_node)
    ast.fix_missing_locations(func_node)
    return func_node
