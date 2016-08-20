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

    def get_uniforms(self):
        uniforms = {}
        stages = (self._vert_shader, self._geom_shader, self._frag_shader)
        for stage in stages:
            for var in stage.get_uniforms():
                if var.name in uniforms and uniforms[var.name] != var:
                    raise KeyError('duplicate uniform: {}'.format(var))
                else:
                    uniforms[var.name] = var
        return uniforms.values()
