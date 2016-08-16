"""Unit test utilities."""

import ast
from unittest import TestCase


def deindent(text):
    """Remove newlines and de-indent the input."""
    lines = text.splitlines()
    out_lines = []
    for line in lines:
        out_lines.append(line.lstrip())
    return ''.join(out_lines)


class AstTestCase(TestCase):
    def assertEqual(self, left, right, msg=None):
        if isinstance(left, ast.AST) and isinstance(right, ast.AST):
            left = ast.dump(left)
            right = ast.dump(right)
        return super(AstTestCase, self).assertEqual(left, right, msg)
