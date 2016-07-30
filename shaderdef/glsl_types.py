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


class mat4: pass
class vec2: pass
class vec3: pass
class vec4: pass
class void: pass
