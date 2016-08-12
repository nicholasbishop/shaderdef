from shaderdef.glsl_types import vec3, vec4

class ShaderInterface(object):
    def __init__(self, **kwargs):
        pass


class GsOut(ShaderInterface):
    gl_position = vec4
    altitudes = vec3
    normal = vec3
