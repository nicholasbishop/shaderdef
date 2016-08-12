from typing import Generic, MutableSequence, TypeVar

from shaderdef.equality import EqualityMixin

class Attribute(EqualityMixin):
    def __init__(self, gtype):
        self.gtype = gtype

    def __repr__(self):
        return 'Attribute({})'.format(self.gtype)

    def glsl_decl(self, name, location=None):
        if location is None:
            layout = ''
        else:
            layout = 'layout(location={}) '.format(location)
        return '{}in {} {};'.format(layout, self.gtype.__name__, name)


class FragOutput(EqualityMixin):
    def __init__(self, gtype):
        self.gtype = gtype

    def __repr__(self):
        return 'FragOutput({})'.format(self.gtype)

    def glsl_decl(self, name):
        return 'out {} {};'.format(self.gtype.__name__, name)


class Uniform(EqualityMixin):
    def __init__(self, gtype):
        self.gtype = gtype

    def __repr__(self):
        return 'Uniform({})'.format(self.gtype)

    def glsl_decl(self, name):
        return 'uniform {} {};'.format(self.gtype.__name__, name)


class BuiltinType(object):
    def __init__(self, *args):
        pass


# pylint: disable=too-many-ancestors


class Indexable(object):
    def __getitem__(self, index):
        pass

    def __setitem__(self, index, val):
        pass

    def __len__(self):
        pass


class Addable(object):
    def __add__(self, other):
        pass


class Mulable(Addable):
    def __mul__(self, other):
        pass


class ShaderInterface(object):
    def __init__(self, **kwargs):
        pass


# TODO
T = TypeVar('T')
class Array3(MutableSequence[T], Indexable):
    def __init__(self, gtype):
        pass

# pylint: disable=invalid-name
class HasXY(Indexable, Mulable):
    @property
    def x(self) -> float:
        pass
    @property
    def y(self) -> float:
        pass
    @property
    def xy(self):
        pass


class HasXYZ(HasXY):
    @property
    def z(self) -> float:
        pass
    @property
    def xyz(self):
        pass


class HasXYZW(HasXYZ):
    @property
    def w(self) -> float:
        pass


class mat2(BuiltinType):
    pass
class mat3(BuiltinType):
    pass
class mat4(BuiltinType, Mulable):
    pass
class vec2(BuiltinType, HasXY):
    pass
class vec3(BuiltinType, HasXYZ):
    pass
class vec4(BuiltinType, HasXYZW):
    pass
class void(BuiltinType):
    pass
# TODO
class noperspective(object):
    pass
