from unittest import TestCase

from shaderdef.glsl_types import vec4, noperspective
from shaderdef.interface import ShaderInterface, UniformBlock

class TestShaderInterface(TestCase):
    def test_declare(self):
        class MyBlock(ShaderInterface):
            var = vec4(noperspective)
        self.assertEqual(list(MyBlock.declare_output_block()),
                         ['out MyBlock {',
                          '    noperspective vec4 var;',
                          '} my_block;'])

    def test_uniform(self):
        class MyBlock2(UniformBlock):
            var = vec4()

        self.assertEqual(list(MyBlock2.declare_input_block('x')),
                         ['uniform MyBlock2 {',
                          '    vec4 var;',
                          '} x;'])
