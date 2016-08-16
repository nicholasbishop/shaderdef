import ast
from inspect import getsource


def ensure_node_is_function(node):
    """Raise a TypeError if node is not a FunctionDef.

    This isn't strictly necessary but makes errors easier to find.
    """
    if not isinstance(node, ast.FunctionDef):
        raise TypeError('input must be an ast.FunctionDef', node)


def get_function_parameters(func_node, include_self=True):
    """Get function parameters and types.

    Return a list of pairs, where each pair is (name, type). Both the
    name and the type are strings, except if no type annotation exists
    the pair will be (name, None).

    Only "regular" parameters are included, not "*args" or similar.

    include_self: if True (the default) then a parameter named "self"
    will be included in the results. Otherwise a parameter named
    "self" will be skipped.
    """
    ensure_node_is_function(func_node)
    params = []
    for arg in func_node.args.args:
        pname = arg.arg
        if not include_self and pname == "self":
            continue

        ptype = None
        if arg.annotation is not None:
            ptype = arg.annotation.id
        params.append((pname, ptype))
    return params


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


def dedent(lines):
    """De-indent based on the first line's indentation."""
    if len(lines) != 0:
        first_lstrip = lines[0].lstrip()
        strip_len = len(lines[0]) - len(first_lstrip)
        for line in lines:
            if len(line[:strip_len].strip()) != 0:
                raise ValueError('less indentation than first line: ' +
                                 line)
            else:
                yield line[strip_len:]


def parse_source(obj):
    src = getsource(obj)
    # TODO(nicholasbishop): this probably doesn't belong here, but
    # it's helpful in the unit tests at least.
    src = '\n'.join(dedent(src.splitlines()))
    return ast.parse(src)


def rename_function(func_node, new_name):
    ensure_node_is_function(func_node)
    func_node.name = new_name


def remove_function_parameters(func_node):
    """Remove all parameters from a function AST node."""
    ensure_node_is_function(func_node)
    func_node.args.args = []


def remove_function_return_type(func_node):
    """Remove return type annotation from a function AST node."""
    ensure_node_is_function(func_node)
    func_node.returns = None
