from unittest import TestCase

from shaderdef.shader import make_prefix

class TestMakePrefix(TestCase):
    def test_vert_shader(self):
        self.assertEqual(make_prefix('vert_shader'), 'vs_')
