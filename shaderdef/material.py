from collections import OrderedDict

from shaderdef.glsl_types import FragOutput
from shaderdef.stage import Stage


class Links(object):
    def __init__(self):
        self.attributes = OrderedDict()
        self.frag_outputs = OrderedDict()
        self.uniforms = OrderedDict()


def find_external_links(material):
    links = Links()
    for key in dir(material):
        val = getattr(material, key)
        if isinstance(val, Attribute):
            links.attributes[key] = val
        elif isinstance(val, FragOutput):
            links.frag_outputs[key] = val
        elif isinstance(val, Uniform):
            links.uniforms[key] = val
    return links


class Material(object):
    def __init__(self):
        # pylint: disable=invalid-name
        self.gl_position = None

    def emit_vertex(self, **kwargs):
        pass
