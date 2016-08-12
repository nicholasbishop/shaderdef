#! /usr/bin/env python3

def indent(line_or_lines):
    if isinstance(line_or_lines, str):
        yield '    ' + line_or_lines
    else:
        for line in line_or_lines:
            yield from indent(line)


def gen_py_class(name, contents):
    yield 'class {}:'.format(name)
    yield from indent(contents)


def gen_py_func(name, args, contents):
    yield 'def {}({}):'.format(name, ', '.join(args))
    yield from indent(contents)


def gen_py_if(condition, body, els=None):
    yield 'if {}:'.format(condition)
    yield from indent(body)
    if els is not None:
        yield 'else:'
        yield from indent(els)


def vec_members(length):
    return ['x', 'y', 'z', 'w'][:length]


class Scalar(object):
    def __init__(self, name, python_type, vec_prefix, mat_prefix=None):
        self.glsl_name = name
        self.class_name = name.capitalize()
        self.python_type = python_type
        self.vec_prefix = vec_prefix
        self.mat_prefix = mat_prefix

    def vec_class_name(self, length):
        return '{}vec{}'.format(self.vec_prefix, length)

    def gen_vec_constructor(self, length):
        members = vec_members(length)
        yield from gen_py_func('__init__', ['self', '*args'], [
            gen_py_if('len(args) == 1', [
                'self.{} = args[0]'.format(name) for name in members
            ], els=[
                # TODO(nicholasbishop): add other valid constructors
                'raise NotImplementedError()'
            ]),
        ])

    def gen_vec_type(self, length):
        yield from gen_py_class(self.vec_class_name(length), [
            self.gen_vec_constructor(length),
            self.gen_vec_swizzles(length)
        ])
        


SCALARS = (
    Scalar('bool', bool, vec_prefix='b'),
    Scalar('int', int, vec_prefix='i'),
    Scalar('uint', int, vec_prefix='u'),
    Scalar('float', float, vec_prefix='', mat_prefix=''),
    Scalar('double', float, vec_prefix='d', mat_prefix='d')
)

def gen_vec_types():
    for scalar in SCALARS:
        for length in (2, 3, 4):
            yield from scalar.gen_vec_type(length)


def main():
    print('\n'.join(list(gen_vec_types())))


if __name__ == '__main__':
    main()
