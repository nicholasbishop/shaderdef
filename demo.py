#! /usr/bin/env python3

from __future__ import print_function

from shaderdef.shader import ShaderDef
from shaderdef.material import Material
from shaderdef.glsl_types import (Attribute, Uniform, FragOutput,
                                  mat4, vec3, vec4)

# pylint: disable=too-many-instance-attributes
class DefaultMaterial(Material):
    def __init__(self):
        super(DefaultMaterial, self).__init__()

        self.vert_loc = Attribute(vec3)
        self.vert_nor = Attribute(vec3)
        self.vert_col = Attribute(vec4)

        self.projection = Uniform(mat4)
        self.camera = Uniform(mat4)
        self.model = Uniform(mat4)

        self.frag_color = FragOutput(vec4)

    @staticmethod
    def perspective_projection(projection: mat4, camera: mat4,
                               model: mat4, point: vec3) -> vec4:
        return projection * camera * model * vec4(point, 1.0)

    def vert_shader(self):
        self.gl_Position = self.perspective_projection(self.projection,
                                                       self.camera,
                                                       self.model,
                                                       self.vert_loc)

    def geom_shader(self):
        pass

    def frag_shader(self):
        # artificial dep test
        self.frag_color = self.vert_col


# TODO
def main():
    shader = ShaderDef(DefaultMaterial())
    shader.translate()
    print(shader.vert_shader)
    print('---')
    print(shader.frag_shader)


if __name__ == '__main__':
    main()
