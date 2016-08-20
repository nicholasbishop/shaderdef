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
                         ['uniform vec4 var;'])

    def test_invalid_type(self):
        class MyBlock3(ShaderInterface):
            # invalid, should be "var = vec4()"
            var = vec4
        with self.assertRaises(TypeError):
            next(MyBlock3.get_vars())
