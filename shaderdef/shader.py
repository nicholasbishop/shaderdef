from ast import fix_missing_locations
from collections import OrderedDict
from shaderdef.ast_util import (find_deps, find_method_ast,
                                make_assign,
                                make_self_attr_load,
                                make_self_attr_store,
                                py_to_glsl,
                                rename_attributes,
                                unselfify)
from shaderdef.glsl_types import Attribute, FragOutput, Uniform


class Links(object):
    def __init__(self):
        self.attributes = OrderedDict()
        self.frag_outputs = OrderedDict()
        self.uniforms = OrderedDict()


class Stage(object):
    def __init__(self, obj, func_name):
        self.name = func_name
        self.ast_root = find_method_ast(obj, func_name)

    def find_deps(self):
        return find_deps(self.ast_root)

    def provide_deps(self, next_stage):
        for dep in next_stage.find_deps().inputs:
            if dep not in self.find_deps().outputs:
                dst = make_self_attr_load(dep)
                src = make_self_attr_store(dep)
                assign = make_assign(dst, src)
                self.ast_root.body.append(assign)

        fix_missing_locations(self.ast_root)

    def required_uniforms(self, all_uniforms):
        for link in self.find_deps().inputs:
            unif = all_uniforms.get(link)
            if unif is not None:
                yield link, unif

    # TODO(nicholasbishop): don't prefix function calls
    def load_names(self, external_links, prefix):
        names = {}
        for link in self.find_deps().inputs:
            unif = external_links.uniforms.get(link)
            # Don't prefix uniforms
            if unif is None:
                names[link] = prefix + link
        return names

    # TODO(nicholasbishop): don't prefix builtins like gl_Position
    # TODO(nicholasbishop): de-dup
    def store_names(self, external_links, prefix):
        names = {}
        for link in self.find_deps().outputs:
            unif = external_links.uniforms.get(link)
            # Don't prefix uniforms
            if unif is None:
                names[link] = prefix + link
        return names

    def to_glsl(self, external_links):
        lines = []
        for link, unif in self.required_uniforms(external_links.uniforms):
            lines.append(unif.glsl_decl(link))
        # TODO(nicholasbishop): fix prefixen
        ast_root = rename_attributes(
            self.ast_root,
            load_names=self.load_names(external_links, 'in_'),
            store_names=self.store_names(external_links, 'vs_'))
        ast_root = unselfify(ast_root)
        lines += py_to_glsl(ast_root)
        return '\n'.join(lines)


class ShaderDef(object):
    def __init__(self, material):
        self._material = material
        self._stages = []
        self._external_links = Links()

        self._init_stages()
        self._init_external_links()
        self._thread_deps()

        # TODO
        self._vert_shader = self._stages[0].to_glsl(self._external_links)
        self._frag_shader = None

    def _init_stages(self):
        # TODO
        stage_names = ('vert_shader', 'frag_shader')
        for name in stage_names:
            self._stages.append(Stage(self._material.__class__, name))

    def _init_external_links(self):
        for key in dir(self._material):
            val = getattr(self._material, key)
            if isinstance(val, Attribute):
                self._external_links.attributes[key] = val
            elif isinstance(val, FragOutput):
                self._external_links.frag_outputs[key] = val
            elif isinstance(val, Uniform):
                self._external_links.uniforms[key] = val

    def _thread_deps(self):
        prev_deps = None
        iter1 = reversed(self._stages)
        iter2 = reversed(self._stages)
        next(iter2)
        for stage, prev_stage in zip(iter1, iter2):
            prev_stage.provide_deps(stage)

    @property
    def vert_shader(self):
        # TODO: do this in the ast
        self._vert_shader = self._vert_shader.replace('vert_shader', 'main')
        # TODO: declare uniforms et al
        return self._vert_shader
