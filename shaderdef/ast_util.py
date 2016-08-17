import ast
from inspect import getsource


def ensure_node_is_function(node):
    """Raise a TypeError if node is not a FunctionDef.

    This isn't strictly necessary but makes errors easier to find.
    """
    if not isinstance(node, ast.FunctionDef):
        raise TypeError('input must be an ast.FunctionDef', node)


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
