import ast

class AttrRename(ast.NodeTransformer):
    # pylint: disable=invalid-name
    def __init__(self, load_names, store_names, call_names):
        self._load_names = load_names
        self._store_names = store_names
        self._call_names = call_names
        self._func_attrs = set()

    def visit_Call(self, node):
        if isinstance(node.func, ast.Attribute):
            self._func_attrs.add(node.func)
        return self.generic_visit(node)

    def visit_Attribute(self, node):
        # Don't transform function names
        if node in self._func_attrs:
            names = self._call_names
        elif isinstance(node.ctx, ast.Load):
            names = self._load_names
        elif isinstance(node.ctx, ast.Store):
            names = self._store_names

        new_name = names.get(node.attr)
        if new_name is not None:
            node.attr = new_name

        return node


def rename_attributes(root, load_names=None, store_names=None,
                      call_names=None):
    if load_names is None:
        load_names = {}
    if store_names is None:
        store_names = {}
    if call_names is None:
        call_names = {}
    return AttrRename(load_names, store_names, call_names).visit(root)
