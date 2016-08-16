import ast

class _Renamer(ast.NodeTransformer):
    # pylint: disable=invalid-name
    def __init__(self, names):
        self.names = names

    def visit_Name(self, node):
        new_name = self.names.get(node.id)
        if new_name is not None:
            node.id = new_name
        return node


def rename_ast_nodes(root_node, names):
    return _Renamer(names).visit(root_node)
