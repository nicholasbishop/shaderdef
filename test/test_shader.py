from unittest import TestCase

from shaderdef.glsl_types import FragOutput, vec4
from shaderdef.shader import ShaderDef
from test.util import deindent


class MyMaterial(object):
    def __init__(self):
        self.color = FragOutput(vec4)

    def vert_shader(self):
        pass

    def frag_shader(self):
        self.color = vec4(1.0, 0.0, 0.0, 1.0)


class TestShader(TestCase):
    def test_simple(self):
        shader = ShaderDef(MyMaterial())
        shader.translate()
        self.assertEqual(deindent(shader.vert_shader),
                         '#version 330 core'
                         'void main() {}')
        self.assertEqual(deindent(shader.frag_shader),
                         '#version 330 core'
                         'out vec4 color;'
                         'void main() {color = vec4(1.0, 0.0, 0.0, 1.0);}')
