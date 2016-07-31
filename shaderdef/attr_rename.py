import ast

class AttrRename(ast.NodeTransformer):
    # pylint: disable=invalid-name
    def __init__(self, load_names, store_names):
        self._load_names = load_names
        self._store_names = store_names
        self._func_names = set()

    def visit_Call(self, node):
        if isinstance(node.func, ast.Attribute):
            self._func_names.add(node.func.attr)
        elif isinstance(node.func, ast.Name):
            self._func_names.add(node.func.id)
        else:
            raise NotImplementedError('unknown call type', node.func)
        return self.generic_visit(node)

    def visit_Attribute(self, node):
        # Don't transform function names
        if node.attr in self._func_names:
            return node

        if isinstance(node.ctx, ast.Load):
            names = self._load_names
        elif isinstance(node.ctx, ast.Store):
            names = self._store_names

        new_name = names.get(node.attr)
        if new_name is not None:
            node.attr = new_name

        return node


def rename_attributes(root, load_names=None, store_names=None):
    if load_names is None:
        load_names = {}
    if store_names is None:
        store_names = {}
    return AttrRename(load_names, store_names).visit(root)
