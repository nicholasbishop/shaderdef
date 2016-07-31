import ast


def make_assign(dst, src):
    return ast.Assign(targets=[dst], value=src)


def make_self_load():
    return ast.Name(ctx=ast.Load(), id='self')


def make_self_attr_load(attr):
    obj = make_self_load()
    return ast.Attribute(attr=attr, ctx=ast.Load(), value=obj)


def make_self_attr_store(attr):
    obj = make_self_load()
    return ast.Attribute(attr=attr, ctx=ast.Store(), value=obj)


def append_to_function_body(func_node, new_node):
    ast.fix_missing_locations(new_node)
    func_node.body.append(new_node)


def rename_function(func_node, new_name):
    if not isinstance(func_node, ast.FunctionDef):
        raise TypeError('input must be an ast.FunctionDef', func_node)
    func_node.name = new_name
