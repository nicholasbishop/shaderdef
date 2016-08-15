import ast

def kwargs_as_assignments(call_node, parent):
    """Yield Assign nodes from kwargs in a Call node."""
    if not isinstance(call_node, ast.Call):
        raise TypeError('node must be an ast.Call')

    if len(call_node.args) > 0:
        raise ValueError('positional args not allowed')

    for keyword in call_node.keywords:
        dst_name = keyword.arg

        if dst_name.startswith('gl_'):
            # Write to builtins directly
            target = [ast.Name(id=keyword.arg, ctx=ast.Load())]
        else:
            # Non-builtins are part of an interface block
            target = [ast.Attribute(value=parent, attr=keyword.arg,
                                    ctx=ast.Store())]

        yield ast.Assign(targets=target, value=keyword.value)


class _RewriteReturn(ast.NodeTransformer):
    def __init__(self, interface):
        self.interface = interface

    def _output_to_list(self, node):
        parent = ast.Name(id=self.interface.instance_name(), ctx=ast.Load())
        return list(kwargs_as_assignments(node.value, parent))

    def visit_Return(self, node):  # pylint: disable=invalid-name
        return self._output_to_list(node)

    def visit_Expr(self, node):  # pylint: disable=invalid-name
        if isinstance(node.value, ast.Yield):
            lst = self._output_to_list(node.value)
            lst.append(ast.parse('EmitVertex()'))
            return lst
        else:
            return node


def rewrite_return_as_assignments(func_node, interface):
    """Modify FunctionDef node to directly assign instead of return."""
    func_node = _RewriteReturn(interface).visit(func_node)
    ast.fix_missing_locations(func_node)
    return func_node
