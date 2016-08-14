from shaderdef.ast_util import parse_source
from shaderdef.stage import Stage, make_prefix


class ShaderDef(object):
    def __init__(self, vert_shader, geom_shader, frag_shader):
        self._vert_shader = Stage(vert_shader)
        self._geom_shader = Stage(geom_shader)
        self._frag_shader = Stage(frag_shader)

    def _thread_deps(self):
        """Link inputs and outputs between stages."""
        iter1 = reversed(self._stages)
        iter2 = reversed(self._stages)
        next(iter2)
        for stage, prev_stage in zip(iter1, iter2):
            stage.input_prefix = make_prefix(prev_stage.name)
            prev_stage.provide_deps(stage)

    def translate(self):
        #self._stages = list(self._create_stages())
        # self._thread_deps()

        # external_links = find_external_links(self._material)

        # # TODO
        # library = parse_source(self._material.__class__)
        self._vert_shader.translate()
        # self._geom_shader = self._stages[1].to_glsl(external_links, library)
        # self._frag_shader = self._stages[2].to_glsl(external_links, library)

    @property
    def vert_shader(self):
        return self._vert_shader.glsl

    @property
    def geom_shader(self):
        if self._geom_shader is None:
            raise ValueError('material has not been translated yet')
        # TODO: declare inputs/outputs
        return self._glsl_geom_shader

    @property
    def frag_shader(self):
        if self._frag_shader is None:
            raise ValueError('material has not been translated yet')
        # TODO: declare inputs/outputs
        return self._glsl_frag_shader
