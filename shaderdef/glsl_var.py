class GlslVar(object):
    """Represent a GLSL variable declaration (or struct member)."""
    def __init__(self, name, gtype):
        self.name = name
        self.gtype = gtype

    def declare(self):
        return '{} {};'.format(self.gtype, self.name)

    def declare_uniform(self):
        return 'uniform {}'.format(self.declare())

    def declare_attribute(self, location=None):
        if location is None:
            location_str = ''
        else:
            location_str = 'layout(location={}) '.format(int(location))
        return '{}in {} {};'.format(location_str, self.gtype, self.name)
