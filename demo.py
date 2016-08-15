#! /usr/bin/env python3

from __future__ import print_function
from typing import Iterator, Sequence

from shaderdef import ShaderInterface
from shaderdef.glsl_types import (Array3, Attribute, Uniform,
                                  gl_triangles, gl_triangle_strip,
                                  mat4, noperspective, vec2, vec3,
                                  vec4)
from shaderdef.glsl_funcs import (end_primitive, exp2, geom_shader_meta,
                                  length, mod)
from shaderdef.shader import ShaderDef


class VertAttrs(ShaderInterface):
    vert_loc = Attribute(vec3())
    vert_nor = Attribute(vec3())
    vert_col = Attribute(vec4())


# TODO
class GlGsIn(ShaderInterface):
    gl_position = vec4()


class View(ShaderInterface):
    projection = Uniform(mat4())
    camera = Uniform(mat4())
    model = Uniform(mat4())
    fb_size = Uniform(vec2())


class VsOut(ShaderInterface):
    gl_position = vec4()
    normal = vec3()
    color = vec4()


class GsOut(ShaderInterface):
    gl_position = vec4()
    altitudes = vec3(noperspective)
    normal = vec3()
    color = vec4()


class FsOut(ShaderInterface):
    color = vec4()


def perspective_projection(projection: mat4, camera: mat4,
                           model: mat4, point: vec3) -> vec4:
    return projection * camera * model * vec4(point, 1.0)


def viewport_to_screen_space(framebuffer_size: vec2, point: vec4) -> vec2:
    """Transform point in viewport space to screen space."""
    return (framebuffer_size * point.xy) / point.w


# Distance of each triangle vertex to the opposite edge
def triangle_2d_altitudes(triangle: Array3[vec2]) -> vec3:
    ed0 = vec2(triangle[2] - triangle[1])
    ed1 = vec2(triangle[2] - triangle[0])
    ed2 = vec2(triangle[1] - triangle[0])

    area = float(abs((ed1.x * ed2.y) -
                     (ed1.y * ed2.x)))

    return vec3(area / length(ed0),
                area / length(ed1),
                area / length(ed2))


def vert_shader(view: View, attr: VertAttrs) -> VsOut:
    return VsOut(gl_position=perspective_projection(view.projection,
                                                    view.camera,
                                                    view.model,
                                                    attr.vert_loc),
                 normal=attr.vert_nor,
                 color=attr.vert_col)


@geom_shader_meta(input_primitive=gl_triangles,
                  output_primitive=gl_triangle_strip,
                  max_vertices=3)
def geom_shader(view: View, gl_in: Sequence[GlGsIn],
                vs_out: Sequence[VsOut]) -> Iterator[GsOut]:
    triangle = Array3[vec2]
    triangle[0] = viewport_to_screen_space(view.fb_size, gl_in[0].gl_position)
    triangle[1] = viewport_to_screen_space(view.fb_size, gl_in[1].gl_position)
    triangle[2] = viewport_to_screen_space(view.fb_size, gl_in[2].gl_position)

    altitudes = vec3(triangle_2d_altitudes(triangle))

    yield GsOut(gl_position=gl_in[0].gl_position,
                altitudes=vec3(altitudes[0], 0, 0),
                normal=vs_out[0].normal,
                color=vs_out[0].normal)

    yield GsOut(gl_position=gl_in[1].gl_position,
                altitudes=vec3(0, altitudes[0], 0),
                normal=vs_out[1].normal,
                color=vs_out[1].normal)

    yield GsOut(gl_position=gl_in[2].gl_position,
                altitudes=vec3(0, 0, altitudes[0]),
                normal=vs_out[2].normal,
                color=vs_out[2].normal)

    end_primitive()


def frag_shader(gs_out: GsOut) -> FsOut:
    color = vec4((gs_out.normal.x + 1.0) * 0.5,
                 (gs_out.normal.y + 1.0) * 0.5,
                 (gs_out.normal.z + 1.0) * 0.5,
                 1.0)

    # Adapted from
    # http://strattonbrazil.blogspot.com/2011/09/single-pass-wireframe-rendering_10.html
    nearest = float(min(min(gs_out.altitudes[0], gs_out.altitudes[1]),
                        gs_out.altitudes[2]))
    edge_intensity = float(1.0 - exp2(-1.0 * nearest * nearest))

    color *= edge_intensity

    # TODO, dijkstra viz hack
    dista = float(gs_out.color[0])

    if dista < 0:
        color *= vec4(0.3, 0.3, 0.3, 1.0)
    else:
        # color[0] = dista;
        rep = float(0.1)
        fac = float(1.0 / rep)
        color[0] = pow(mod(gs_out.color[0], rep) * fac, 4)

    return FsOut(color=color)


def main():
    sdef = ShaderDef(vert_shader=vert_shader,
                     geom_shader=geom_shader,
                     frag_shader=frag_shader)
    sdef.translate()
    print(sdef.vert_shader)
    print('---')
    print(sdef.geom_shader)
    print('---')
    print(sdef.frag_shader)


if __name__ == '__main__':
    main()
