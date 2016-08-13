#! /usr/bin/env python3

from itertools import combinations_with_replacement, product

def indent(line_or_lines):
    if isinstance(line_or_lines, str):
        yield '    ' + line_or_lines
    else:
        for line in line_or_lines:
            yield from indent(line)


def gen_py_class(name, contents):
    yield 'class {}:'.format(name)
    yield from indent(contents)


def gen_py_func(name, args, contents, ret=None):
    if ret is None:
        ret_str = ''
    else:
        ret_str = ' -> {}'.format(ret)
    yield 'def {}({}){}:'.format(name, ', '.join(args), ret_str)
    yield from indent(contents)


def gen_py_if(condition, body, els=None):
    yield 'if {}:'.format(condition)
    yield from indent(body)
    if els is not None:
        yield 'else:'
        yield from indent(els)


class Scalar(object):
    def __init__(self, name, python_type, vec_prefix, mat_prefix=None,
                 default=None):
        self.class_name = name
        self.python_type = python_type
        self.vec_prefix = vec_prefix
        self.mat_prefix = mat_prefix
        self.default = default


class Vector(object):
    def __init__(self, scalar, length):
        self.scalar = scalar
        self.length = length
        self.class_name = '{}vec{}'.format(scalar.vec_prefix, length)
        self.members = ['x', 'y', 'z', 'w'][:length]

    def gen_py_constructor(self):
        default = self.scalar.default
        yield from gen_py_func('__init__', ['self', '*args'], [
            gen_py_if('len(args) == 1 and is_scalar(args[0])', [
                'self._{} = {}'.format(name, default) for name in self.members
            ], els=[
                # TODO(nicholasbishop): add other valid constructors
                'raise NotImplementedError()'
            ]),
        ])

    def gen_swizzles(self):
        for length in range(2, self.length + 1):
            for name in combinations_with_replacement(self.members, length):
                ret_type = find_vec_type(self.scalar, length).class_name
                ret_type_ctor = ret_type
                if ret_type == self.class_name:
                    # Forward declaration
                    ret_type = '"{}"'.format(ret_type)
                ctor_args = ['self._{}'.format(elem) for elem in name]
                yield '@property'
                yield from gen_py_func(
                    ''.join(name), ['self'],
                    'return {}({})'.format(ret_type_ctor,
                                           ', '.join(ctor_args)),
                    ret=ret_type
                )

    def gen_py_class(self):
        yield from gen_py_class(self.class_name, [
            self.gen_py_constructor(),
            self.gen_swizzles()
        ])


SCALARS = [
    Scalar('bool', bool, vec_prefix='b', default=False),
    Scalar('int', int, vec_prefix='i', default=0),
    Scalar('uint', int, vec_prefix='u', default=0),
    Scalar('float', float, vec_prefix='', mat_prefix='', default=0.0),
    Scalar('double', float, vec_prefix='d', mat_prefix='d', default=0.0)
]

VECTOR_LENGTHS = [2, 3, 4]

VECTORS = [
    Vector(scalar, length)
    for scalar, length
    in product(SCALARS, VECTOR_LENGTHS)
]

def find_vec_type(scalar, length):
    for vec in VECTORS:
        if vec.scalar == scalar and vec.length == length:
            return vec


def gen_vec_types():
    for scalar in SCALARS:
        for length in (2, 3, 4):
            vector = Vector(scalar, length)
            yield from vector.gen_py_class()


def gen_is_scalar():
    stypes = [scalar.class_name for scalar in SCALARS]
    yield from gen_py_func(
        'is_scalar', ['var: Any'],
        ['return isinstance(var, ({}))'.format(', '.join(stypes))],
         ret='bool')


def gen_scalar_types():
    for scalar in SCALARS:
        if scalar.class_name == scalar.python_type.__name__:
            continue
        yield from gen_py_class(scalar.class_name, [
            gen_py_func(
                '__init__',
                ['self', 'val: {}={}'.format(scalar.python_type.__name__,
                                             scalar.default)],
                ['self._val = val'],
                ret='None'
            )
        ])


BLANK_LINE = ''


def gen_imports():
    yield 'from typing import Any'
    yield BLANK_LINE


def main():
    code = []
    code += gen_imports()
    code += gen_is_scalar()
    code += gen_scalar_types()
    code += gen_vec_types()

    print('\n'.join(list(code)))


if __name__ == '__main__':
    main()
