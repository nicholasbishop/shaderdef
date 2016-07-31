import ast
from inspect import getsource

class Code(object):
    def __init__(self, initial_line=None):
        self.lines = []
        if initial_line is not None:
            self.lines.append(initial_line)
        self._indent_string = '    '

    def __call__(self, line):
        self.lines.append(line)

    def indent(self, code):
        for line in code.lines:
            self.lines.append(self._indent_string + line)

    def one(self):
        if len(self.lines) != 1:
            raise ValueError('expected exactly one line', self)
        return self.lines[0]


class AstToGlsl(ast.NodeVisitor):
    # pylint: disable=invalid-name
    def visit_Module(self, node):
        if len(node.body) != 1:
            raise NotImplementedError()
        child = node.body[0]
        return self.visit(child)

    def visit_FunctionDef(self, node):
        if getattr(node, 'returns', None) is None:
            return_type = 'void'
        else:
            return_type = self.visit(node.returns).one()
        params = node.args.args[1:]  # skip self
        params = (self.visit(param).one() for param in params)
        code = Code()
        code('{} {}({}) {{'.format(return_type, node.name,
                                   ', '.join(params)))
        for child in node.body:
            code.indent(self.visit(child))
        code('}')
        return code

    def visit_arg(self, node):
        gtype = self.visit(node.annotation).one()
        return Code('{} {}'.format(gtype, node.arg))

    def visit_Name(self, node):
        # pylint: disable=no-self-use
        return Code(node.id)

    def visit_Attribute(self, node):
        return Code('{}.{}'.format(self.visit(node.value).one(), node.attr))

    def visit_Assign(self, node):
        if len(node.targets) != 1:
            raise ValueError('multiple assignment targets not allowed', node)
        target = node.targets[0]
        return Code('{} = {};'.format(self.visit(target).one(),
                                      self.visit(node.value).one()))

    def visit_Num(self, node):
        # pylint: disable=no-self-use
        return Code(str(node.n))

    def visit_Call(self, node):
        args = (self.visit(arg).one() for arg in node.args)
        name = self.visit(node.func).one()
        return Code('{}({})'.format(name, ', '.join(args)))

    def visit_Return(self, node):
        return Code('return {};'.format(self.visit(node.value).one()))

# src = getsource(myFunc)
# node = ast.parse(src)


class FindMethodVisitor(ast.NodeVisitor):
    # pylint: disable=invalid-name
    def __init__(self, method):
        super(FindMethodVisitor, self).__init__()
        self._method = method

    def visit_Module(self, node):
        return self.visit_children(node)

    def visit_ClassDef(self, node):
        return self.visit_children(node)

    def visit_FunctionDef(self, node):
        if node.name == self._method:
            return node

    def visit_children(self, node):
        for child in node.body:
            result = self.visit(child)
            if result is not None:
                return result


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


def py_to_glsl(node):
    # TODO
    #print_ast(node)

    atg = AstToGlsl()
    code = atg.visit(node)
    # TODO
    return code.lines


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
