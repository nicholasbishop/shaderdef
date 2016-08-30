#! /usr/bin/env python3

"""This demo shows how to define a very simple shader program with a
vertex shader and a fragment shader.

The vertex shader is defined in the `vert_shader` function. Note that
the inputs and outputs are annotated; this is how shaderdef knows
what types to use in the generated GLSL code.

Inputs and outputs are grouped together using a Python class. For
example, this shader program's vertex attributes are defined in
`VsIn`. It inherits from `AttributeBlock` to mark its members as vertex
attributes. (There's a UniformBlock for declaring uniform inputs.)

Shader outputs are set using the `return` keyword. The return type
should be a class such as `VsOut`; pass the outputs as keyword
arguments.
"""

from shaderdef import (AttributeBlock, FragmentShaderOutputBlock,
                       ShaderDef, ShaderInterface)

from shaderdef.glsl_types import vec2, vec4


class VsIn(AttributeBlock):
    position = vec2()

class VsOut(ShaderInterface):
    gl_position = vec4()

class FsOut(FragmentShaderOutputBlock):
    color = vec4()

def vert_shader(attr: VsIn) -> VsOut:
    return VsOut(gl_position=vec4(-attr.position.x, attr.position.y, 1.0, 1.0))

def frag_shader() -> FsOut:
    return FsOut(color=vec4(1.0, 0.0, 0.0, 1.0))

def print_shaders():
    sdef = ShaderDef(vert_shader=vert_shader, frag_shader=frag_shader)
    sdef.translate()

    print('\nvertex shader:')
    print('--------------')
    print(sdef.vert_shader)
    print('\nfragment shader:')
    print('----------------')
    print(sdef.frag_shader)

def main():
    """
    >>> print_shaders()  # doctest: +NORMALIZE_WHITESPACE
    vertex shader:
    --------------
    #version 330 core
    layout(location=0) in vec2 position;
    void main() {
        gl_Position = vec4(-attr.position.x, attr.position.y, 1.0, 1.0);
    }
    fragment shader:
    ----------------
    #version 330 core
    layout(location=0) out vec4 color;
    void main() {
        color = vec4(1.0, 0.0, 0.0, 1.0);
    }
    """
    print_shaders()


if __name__ == '__main__':
    main()
