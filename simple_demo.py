#! /usr/bin/env python3

"""
>>> sdef = ShaderDef(vert_shader=vert_shader, frag_shader=frag_shader)
>>> sdef.translate()

>>> print(sdef.vert_shader)
#version 330 core
layout(location=0) in vec2 position;
void main() {
    gl_Position = vec4(-attr.position.x, attr.position.y, 1.0, 1.0);
}

>>> print(sdef.frag_shader)
#version 330 core
layout(location=0) out vec4 color;
void main() {
    color = vec4(1.0, 0.0, 0.0, 1.0);
}
"""

from shaderdef import (AttributeBlock, FragmentShaderOutputBlock,
                       ShaderDef, ShaderInterface)

from shaderdef.glsl_types import vec2, vec4


class VsIn(AttributeBlock):
    position = vec2()

class VsOut(ShaderInterface):
    gl_position = vec2()

class FsOut(FragmentShaderOutputBlock):
    color = vec4()

def vert_shader(attr: VsIn) -> VsOut:
    return VsOut(gl_position=vec4(-attr.position.x, attr.position.y, 1.0, 1.0))

def frag_shader() -> FsOut:
    return FsOut(color=vec4(1.0, 0.0, 0.0, 1.0))


def main():
    sdef = ShaderDef(vert_shader=vert_shader, frag_shader=frag_shader)
    sdef.translate()
    print('\nvertex shader:')
    print('--------------')
    print(sdef.vert_shader)

    print('\nfragment shader:')
    print('----------------')
    print(sdef.frag_shader)


if __name__ == '__main__':
    main()
