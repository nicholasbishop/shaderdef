def _gdecl(*parts):
    not_none = (part for part in parts if part is not None)
    return '{};'.format(' '.join(not_none))


def location_str(location):
    if location is None:
        return None
    else:
        return 'layout(location={})'.format(int(location))


class GlslVar(object):
    """Represent a GLSL variable declaration (or struct member)."""
    def __init__(self, name, gtype, interpolation=None):
        self.name = name
        self.gtype = gtype
        self.interpolation = interpolation

    def declare(self):
        return _gdecl(self.interpolation, self.gtype, self.name)

    def declare_uniform(self):
        return _gdecl('uniform', self.gtype, self.name)

    def declare_attribute(self, location=None):
        return _gdecl(location_str(location), self.interpolation,
                      'in', self.gtype, self.name)

    def declare_output(self, location=None):
        return _gdecl(self.interpolation, location_str(location),
                      'out', self.gtype, self.name)
