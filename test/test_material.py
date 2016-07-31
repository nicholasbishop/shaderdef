from unittest import TestCase

from shaderdef.glsl_types import Attribute, FragOutput, Uniform, vec4
from shaderdef.material import find_external_links


class TestFindExternalLinks(TestCase):
    def setUp(self):
        class MyMaterial(object):
            def __init__(self):
                self.myattr = Attribute(vec4)
                self.myout = FragOutput(vec4)
                self.myunif = Uniform(vec4)

        self.material = MyMaterial()

    def test_links(self):
        links = find_external_links(self.material)
        self.assertEqual(links.attributes, {'myattr': Attribute(vec4)})
        self.assertEqual(links.frag_outputs, {'myout': FragOutput(vec4)})
        self.assertEqual(links.uniforms, {'myunif': Uniform(vec4)})
