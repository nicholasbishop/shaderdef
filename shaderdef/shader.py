import attr
from shaderdef.stage import Stage


@attr.s(init=False)
class ShaderDef(object):
    def __init__(self, vert_shader, frag_shader, geom_shader=None):
        self._library = []
        self._vert_shader = Stage(vert_shader)
        self._frag_shader = Stage(frag_shader)
        if geom_shader is None:
            self._geom_shader = None
        else:
            self._geom_shader = Stage(geom_shader)

    def add_function(self, function):
        """Add a utility `function` to the shader program.

        Each utility function is currently emitted in all shader
        stages regardless of which stage or stages the function is
        actually used in.
        """
        self._library.append(function)

    def translate(self):
        self._vert_shader.translate(self._library)
        self._frag_shader.translate(self._library)
        if self._geom_shader is not None:
            self._geom_shader.translate(self._library)

    @property
    def vert_shader(self):
        """Get the GLSL code for the vertex shader."""
        return self._vert_shader.glsl

    @property
    def geom_shader(self):
        """Get the GLSL code for the geometry shader."""
        if self._geom_shader is None:
            raise ValueError('this shaderdef does not have a geometry shader')
        return self._geom_shader.glsl

    @property
    def frag_shader(self):
        """Get the GLSL code for the fragment shader."""
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
