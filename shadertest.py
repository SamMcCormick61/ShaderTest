import time, pyglet, moderngl
import numpy as np

# ---------- window & context ----------
win = pyglet.window.Window(width=800, height=800, caption="Shader demo")
ctx = moderngl.create_context()

# ---------- geometry (full‑screen quad) ----------
vbo = ctx.buffer(np.array([
    -1,-1,  1,-1, -1,1,
     1,-1,  1, 1, -1,1
], dtype='f4'))
prog = ctx.program(
    vertex_shader="""
        #version 330
        layout(location = 0) in vec2 in_position;
        out vec2 uv;
        void main() {
            uv = in_position*0.5 + 0.5;
            gl_Position = vec4(in_position, 0.0, 1.0);
        }
    """,
    fragment_shader="""
        #version 330
        in  vec2 uv;
        uniform float iTime;
        out vec4 frag_colour;
        void main() {
            float c = 0.5 + 0.5*sin(10.0*length(uv-0.5) - iTime);
            frag_colour = vec4(vec3(c), 1.0);
        }
    """
)
vao = ctx.simple_vertex_array(prog, vbo, 'in_position')

# ---------- draw callback ----------
@win.event
def on_draw():
    ctx.clear(0.0, 0.0, 0.0, 1.0)
    prog['iTime'] = time.perf_counter()          # seconds since start
    vao.render(moderngl.TRIANGLES)

# start 60 fps loop (pyglet’s default)
pyglet.app.run()
