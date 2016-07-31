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
    pass


# pylint: disable=invalid-name
class mat2(BuiltinType):
    pass
class mat3(BuiltinType):
    pass
class mat4(BuiltinType):
    pass
class vec2(BuiltinType):
    pass
class vec3(BuiltinType):
    pass
class vec4(BuiltinType):
    pass
class void(BuiltinType):
    pass
