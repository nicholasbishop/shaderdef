import ast


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

    def visit_Pass(self, _):
        # pylint: disable=no-self-use
        return Code()

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

    def visit_Expr(self, node):
        return self.visit(node.value)

    def visit_BinOp(self, node):
        # TODO(nicholasbishop): FloorDiv, Pow, LShift, RShift,
        # BitOr, BitXor, BitAnd
        ops = {
            ast.Add: '+',
            ast.Sub: '-',
            ast.Mult: '*',
            ast.Div: '/',
            ast.Mod: '%',
        }
        if hasattr(ast, 'MatMult'):
            ops[ast.MatMult] = '*'
        return Code('({} {} {})'.format(
            self.visit(node.left).one(),
            ops[node.op.__class__],
            self.visit(node.right).one(),
        ))


def py_to_glsl(root):
    """Translate Python AST into GLSL code.

    root: an ast.FunctionDef object

    Return a list of strings, where each string is a line of GLSL
    code.
    """
    atg = AstToGlsl()
    code = atg.visit(root)
    return code.lines
