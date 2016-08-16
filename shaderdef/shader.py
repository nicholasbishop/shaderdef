from shaderdef.stage import Stage


class ShaderDef(object):
    def __init__(self, vert_shader, geom_shader, frag_shader):
        self._vert_shader = Stage(vert_shader)
        self._geom_shader = Stage(geom_shader)
        self._frag_shader = Stage(frag_shader)
        self._library = []

    def add_function(self, func):
        self._library.append(func)

    def translate(self):
        self._vert_shader.translate(self._library)
        self._geom_shader.translate(self._library)
        self._frag_shader.translate(self._library)

    @property
    def vert_shader(self):
        return self._vert_shader.glsl

    @property
    def geom_shader(self):
        return self._geom_shader.glsl

    @property
    def frag_shader(self):
        return self._frag_shader.glsl
