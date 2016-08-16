from unittest import TestCase

from shaderdef.glsl_types import vec4, noperspective
from shaderdef.interface import ShaderInterface

class TestShaderInterface(TestCase):
    def test_declare(self):
        class MyBlock(ShaderInterface):
            var = vec4(noperspective)
        self.assertEqual(list(MyBlock.glsl_declaration('out')),
                         ['out MyBlock {',
                          '    noperspective vec4 var;',
                          '} my_block;'])
