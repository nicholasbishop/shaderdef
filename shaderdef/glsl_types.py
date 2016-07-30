class Attribute(object):
    def __init__(self, gtype):
        pass


class FragOutput(object):
    def __init__(self, gtype):
        pass


class Uniform(object):
    def __init__(self, gtype):
        self.gtype = gtype

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
