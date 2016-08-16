from unittest import TestCase

from shaderdef.stage import Stage, make_prefix

class TestMakePrefix(TestCase):
    def test_vert_shader(self):
        self.assertEqual(make_prefix('vert_shader'), 'vs_')


class TestAuxFunction(TestCase):
    # pylint: disable=unused-argument
    def test_library(self):
        def simple_stage():
            pass

        def aux(self):
            pass

        stage = Stage(simple_stage)
        code = stage.to_glsl([aux])
        self.assertIn('void aux() {', code)
