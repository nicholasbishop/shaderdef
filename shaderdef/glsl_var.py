def _gdecl(*parts):
    not_none = (part for part in parts if part is not None)
    return '{};'.format(' '.join(not_none))


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
        if location is None:
            location_str = None
        else:
            location_str = 'layout(location={})'.format(int(location))

        return _gdecl(location_str, self.interpolation, 'in', self.gtype,
                      self.name)

    def declare_output(self):
        return _gdecl(self.interpolation, 'out', self.gtype, self.name)
