from subprocess import check_output
import sys
from unittest import TestCase

DEMO_EXPECTED = """#version 330 core
layout(location=0) in vec3 vert_loc;
layout(location=1) in vec3 vert_nor;
layout(location=2) in vec4 vert_col;
uniform mat4 projection;
uniform mat4 camera;
uniform mat4 model;
uniform vec2 fb_size;
vec4 perspective_projection(mat4 projection, mat4 camera, mat4 model, vec3 point) {
    return (((projection * camera) * model) * vec4(point, 1.0));
}
vec2 viewport_to_screen_space(vec2 framebuffer_size, vec4 point) {
    return ((framebuffer_size * point.xy) / point.w);
}
vec3 triangle_2d_altitudes(vec2 triangle[3]) {
    vec2 ed0 = vec2((triangle[2] - triangle[1]));
    vec2 ed1 = vec2((triangle[2] - triangle[0]));
    vec2 ed2 = vec2((triangle[1] - triangle[0]));
    float area = float(abs(((ed1.x * ed2.y) - (ed1.y * ed2.x))));
    return vec3((area / length(ed0)), (area / length(ed1)), (area / length(ed2)));
}
out VsOut {
    vec3 normal;
    vec4 color;
} vs_out;
void main() {
    gl_Position = perspective_projection(projection, camera, model, vert_loc);
    vs_out.normal = vert_nor;
    vs_out.color = vert_col;
}
---
#version 330 core
layout(triangles) in;
layout(triangle_strip, max_vertices = 3) out;
uniform mat4 projection;
uniform mat4 camera;
uniform mat4 model;
uniform vec2 fb_size;
in VsOut {
    vec3 normal;
    vec4 color;
} vs_out[];
vec4 perspective_projection(mat4 projection, mat4 camera, mat4 model, vec3 point) {
    return (((projection * camera) * model) * vec4(point, 1.0));
}
vec2 viewport_to_screen_space(vec2 framebuffer_size, vec4 point) {
    return ((framebuffer_size * point.xy) / point.w);
}
vec3 triangle_2d_altitudes(vec2 triangle[3]) {
    vec2 ed0 = vec2((triangle[2] - triangle[1]));
    vec2 ed1 = vec2((triangle[2] - triangle[0]));
    vec2 ed2 = vec2((triangle[1] - triangle[0]));
    float area = float(abs(((ed1.x * ed2.y) - (ed1.y * ed2.x))));
    return vec3((area / length(ed0)), (area / length(ed1)), (area / length(ed2)));
}
out GsOut {
    noperspective vec3 altitudes;
    vec3 normal;
    vec4 color;
} gs_out;
void main() {
    vec2 triangle[3];
    triangle[0] = viewport_to_screen_space(fb_size, gl_in[0].gl_Position);
    triangle[1] = viewport_to_screen_space(fb_size, gl_in[1].gl_Position);
    triangle[2] = viewport_to_screen_space(fb_size, gl_in[2].gl_Position);
    vec3 altitudes = vec3(triangle_2d_altitudes(triangle));
    gl_Position = gl_in[0].gl_Position;
    gs_out.altitudes = vec3(altitudes[0], 0, 0);
    gs_out.normal = vs_out[0].normal;
    gs_out.color = vs_out[0].color;
    EmitVertex();
    gl_Position = gl_in[1].gl_Position;
    gs_out.altitudes = vec3(0, altitudes[1], 0);
    gs_out.normal = vs_out[1].normal;
    gs_out.color = vs_out[1].color;
    EmitVertex();
    gl_Position = gl_in[2].gl_Position;
    gs_out.altitudes = vec3(0, 0, altitudes[2]);
    gs_out.normal = vs_out[2].normal;
    gs_out.color = vs_out[2].color;
    EmitVertex();
    EndPrimitive();
}
---
#version 330 core
in GsOut {
    noperspective vec3 altitudes;
    vec3 normal;
    vec4 color;
} gs_out;
vec4 perspective_projection(mat4 projection, mat4 camera, mat4 model, vec3 point) {
    return (((projection * camera) * model) * vec4(point, 1.0));
}
vec2 viewport_to_screen_space(vec2 framebuffer_size, vec4 point) {
    return ((framebuffer_size * point.xy) / point.w);
}
vec3 triangle_2d_altitudes(vec2 triangle[3]) {
    vec2 ed0 = vec2((triangle[2] - triangle[1]));
    vec2 ed1 = vec2((triangle[2] - triangle[0]));
    vec2 ed2 = vec2((triangle[1] - triangle[0]));
    float area = float(abs(((ed1.x * ed2.y) - (ed1.y * ed2.x))));
    return vec3((area / length(ed0)), (area / length(ed1)), (area / length(ed2)));
}
layout(location=0) out vec4 fs_color;
void main() {
    vec4 color = vec4(((gs_out.normal.x + 1.0) * 0.5), ((gs_out.normal.y + 1.0) * 0.5), ((gs_out.normal.z + 1.0) * 0.5), 1.0);
    float nearest = float(min(min(gs_out.altitudes[0], gs_out.altitudes[1]), gs_out.altitudes[2]));
    float edge_intensity = float((1.0 - exp2(((-1.0 * nearest) * nearest))));
    color *= edge_intensity;
    float dista = float(gs_out.color[0]);
    if (dista < 0) {
        color *= vec4(0.3, 0.3, 0.3, 1.0);
    } else {
        float rep = float(0.1);
        float fac = float((1.0 / rep));
        color[0] = pow((mod(gs_out.color[0], rep) * fac), 4);
    }
    fs_color = color;
}
"""

class TestDemo(TestCase):
    def test_demo_output(self):
        """Test to ensure that the demo output doesn't change.

        This could obviously be a bit fragile, but better than
        accidentally breaking the demo.
        """
        cmd = (sys.executable, '-m', 'demo')
        self.assertEqual(check_output(cmd).decode(), DEMO_EXPECTED)
