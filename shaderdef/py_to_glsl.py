import ast
from shaderdef.glsl_types import ArraySpec

class Code(object):
    def __init__(self, initial_line=None):
        self.lines = []
        if initial_line is not None:
            self.lines.append(initial_line)
        self._indent_string = '    '

    def __call__(self, line):
        self.lines.append(line)

    def append_block(self, code):
        for line in code.lines:
            line = self._indent_string + line
            if line[-1] not in (';', '{', '}'):
                line += ';'
            self.lines.append(line)

    def one(self):
        if len(self.lines) != 1:
            raise ValueError('expected exactly one line', self)
        return self.lines[0]


def op_symbol(op_node):
    """Get the GLSL symbol for a Python operator."""
    ops = {
        # TODO(nicholasbishop): other unary ops
        ast.UAdd: '+',
        ast.USub: '-',

        # TODO(nicholasbishop): FloorDiv, Pow, LShift, RShift,
        # BitOr, BitXor, BitAnd
        ast.Add: '+',
        ast.Sub: '-',
        ast.Mult: '*',
        ast.Div: '/',
        ast.Mod: '%',

        # Comparison
        ast.Eq: '=',
        ast.NotEq: '!=',
        ast.Lt: '<',
        ast.LtE: '<=',
        ast.Gt: '>',
        ast.GtE: '>=',
    }
    # Python3 matrix multiplication
    if hasattr(ast, 'MatMult'):
        ops[ast.MatMult] = '*'
    return ops[op_node.__class__]


class AstToGlsl(ast.NodeVisitor):
    # pylint: disable=invalid-name,too-many-public-methods
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
        params = node.args.args[:]
        # Skip self
        if len(params) != 0 and params[0].arg == 'self':
            params = params[1:]
        params = (self.visit(param).one() for param in params)
        code = Code()
        code('{} {}({}) {{'.format(return_type, node.name,
                                   ', '.join(params)))
        for child in node.body:
            code.append_block(self.visit(child))
        code('}')
        return code

    def visit_Pass(self, _):
        # pylint: disable=no-self-use
        return Code()

    def visit_arg(self, node):
        if node.annotation is None:
            raise ValueError('untyped argument: {}'.format(ast.dump(node)))
        adecl = ArraySpec.from_ast_node(node.annotation)
        if adecl is not None:
            return Code('{} {}[{}]'.format(adecl.element_type, node.arg,
                                           adecl.length))

        gtype = self.visit(node.annotation).one()
        return Code('{} {}'.format(gtype, node.arg))

    def visit_Name(self, node):
        # pylint: disable=no-self-use
        return Code(node.id)

    def visit_Attribute(self, node):
        return Code('{}.{}'.format(self.visit(node.value).one(), node.attr))

    @staticmethod
    def is_var_decl(node):
        target = node.targets[0]
        return (isinstance(target, ast.Name) and
                not target.id.startswith('gl_') and
                isinstance(node.value, ast.Call))

    def get_array_decl(self, node):
        # TODO(nicholasbishop): clean mess up
        target = node.targets[0]
        aspec = ArraySpec.from_ast_node(node.value)
        if aspec is None:
            return None
        return Code('{} {}[{}]'.format(aspec.element_type,
                                       self.visit(target).one(),
                                       aspec.length))

    def make_var_decl(self, node):
        target = node.targets[0]
        gtype = node.value.func.id
        return Code('{} {} = {}'.format(gtype,
                                        self.visit(target).one(),
                                        self.visit(node.value).one()))

    def visit_Assign(self, node):
        if len(node.targets) != 1:
            raise ValueError('multiple assignment targets not allowed', node)
        target = node.targets[0]
        if self.is_var_decl(node):
            return self.make_var_decl(node)
        adecl = self.get_array_decl(node)
        if adecl is not None:
            return adecl
        return Code('{} = {}'.format(self.visit(target).one(),
                                     self.visit(node.value).one()))

    def visit_Num(self, node):
        # pylint: disable=no-self-use
        return Code(str(node.n))

    def visit_Call(self, node):
        args = (self.visit(arg).one() for arg in node.args)
        name = self.visit(node.func).one()
        return Code('{}({})'.format(name, ', '.join(args)))

    def visit_Return(self, node):
        return Code('return {}'.format(self.visit(node.value).one()))

    def visit_Expr(self, node):
        return self.visit(node.value)

    def visit_Str(self, node):
        # pylint: disable=no-self-use,unused-argument
        return Code()

    def visit_UnaryOp(self, node):
        return Code('{}{}'.format(op_symbol(node.op),
                                  self.visit(node.operand).one()))

    def visit_BinOp(self, node):
        return Code('({} {} {})'.format(
            self.visit(node.left).one(),
            op_symbol(node.op),
            self.visit(node.right).one(),
        ))

    def visit_Subscript(self, node):
        return Code('{}{}'.format(self.visit(node.value).one(),
                                  self.visit(node.slice).one()))

    def visit_Index(self, node):
        return Code('[{}]'.format(self.visit(node.value).one()))

    def visit_AugAssign(self, node):
        return Code('{} {}= {}'.format(self.visit(node.target).one(),
                                       op_symbol(node.op),
                                       self.visit(node.value).one()))

    def visit_Compare(self, node):
        if len(node.ops) != 1 or len(node.comparators) != 1:
            raise NotImplementedError('only one op/comparator is supported',
                                      node)
        op = node.ops[0]
        right = node.comparators[0]
        return Code('{} {} {}'.format(self.visit(node.left).one(),
                                      op_symbol(op),
                                      self.visit(right).one()))

    def visit_If(self, node):
        code = Code('if ({}) {{'.format(self.visit(node.test).one()))
        for child in node.body:
            code.append_block(self.visit(child))
        # TODO(nicholasbishop): emit "else if" to make output cleaner
        if len(node.orelse) != 0:
            code('} else {')
            for child in node.orelse:
                code.append_block(self.visit(child))
        code('}')
        return code

    def visit_For(self, node):
        if not isinstance(node.target, ast.Name):
            raise NotImplementedError('for-loop target must be an ast.Name')
        itr = node.iter
        if not isinstance(itr, ast.Call) or itr.func.id != 'range':
            raise NotImplementedError('only range() for loops are supported')
        if len(itr.args) != 1 or not isinstance(itr.args[0], ast.Num):
            raise NotImplementedError('only 0..n for loops are supported')
        end = self.visit(itr.args[0]).one()
        var = self.visit(node.target).one()
        code = Code()
        code('for (int {var} = 0; {var} < {end}; {var}++) {{'.format(var=var,
                                                                     end=end))
        for child in node.body:
            code.append_block(self.visit(child))
        code('}')
        return code

    def visit(self, node):
        ret = super().visit(node)
        if ret is None:
            raise KeyError('unhandled ast node type',
                           ast.dump(node))
        else:
            return ret


def py_to_glsl(root):
    """Translate Python AST into GLSL code.

    root: an ast.FunctionDef object

    Return a list of strings, where each string is a line of GLSL
    code.
    """
    atg = AstToGlsl()
    code = atg.visit(root)
    return code.lines
