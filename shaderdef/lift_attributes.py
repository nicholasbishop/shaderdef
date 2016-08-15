import ast

class _LiftAttributes(ast.NodeTransformer):
    def __init__(self, objects):
        self._objects = objects

    # pylint: disable=invalid-name
    def visit_Attribute(self, node):
        value = node.value
        if isinstance(value, ast.Name) and value.id in self._objects:
            return ast.Name(id=node.attr, ctx=node.ctx)
        else:
            return node


def lift_attributes(func_node, objects):
    return _LiftAttributes(objects).visit(func_node)
