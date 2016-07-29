from __future__ import print_function

from shaderdef.shader import ShaderDef
from shaderdef.glsl_types import (Attribute, Uniform, FragOutput,
                                  mat4, vec3, vec4)

class DefaultMaterial(object):
    def __init__(self):
        self.vert_loc = Attribute(vec3)
        self.vert_nor = Attribute(vec3)
        self.vert_col = Attribute(vec4)

        self.projection = Uniform(mat4)
        self.camera = Uniform(mat4)
        self.model = Uniform(mat4)

        self.frag_color = FragOutput(vec4)

    def vert_shader(self):
        self.gl_Position = self.perspective_projection(self.projection,
                                                       self.camera,
                                                       self.model,
                                                       self.vert_loc)

    def frag_shader(self):
        # artificial dep test
        self.frag_color = self.vert_col


# TODO

shader = ShaderDef(DefaultMaterial())
print(shader.vert_shader)
