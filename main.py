import moderngl_window as mglw
import moderngl
import numpy as np
import effect1.shader

class Back2Basic(mglw.WindowConfig):
    gl_version = (3, 3)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.currentShader = effect1.shader.getShader(self.ctx)
        x = np.linspace(-1.0, 1.0, 50)
        y = np.random.rand(50) - 0.5
        r = np.ones(50)
        g = np.zeros(50)
        b = np.zeros(50)
        t = np.zeros(50)

        self.vertices = np.dstack([x, y, r, g, b, t])
        self.vbo = self.ctx.buffer(self.vertices.astype('f4').tobytes())
        self.vao = self.ctx.vertex_array(self.currentShader, [
            (self.vbo, "2f 3f 1f", 'in_vert', 'in_color', 'in_time')
        ])

    def render(self, time, frametime):
        self.ctx.clear(0.0, 0.0, 0.0, 1.0)
        self.vao.render(moderngl.LINE_STRIP)

        self.vertices[0, :, 5] = np.repeat(time, 50)
        self.vbo = self.ctx.buffer(self.vertices.astype('f4').tobytes())
        self.vao = self.ctx.vertex_array(self.currentShader, [
            (self.vbo, "2f 3f 1f", 'in_vert', 'in_color', 'in_time')
        ])
        # if(self.scheduler(time)):
        #     print("finished")
        #     exit()

    def scheduler(self, time):
        if(time < 4):
            print("Effect 1")
        elif(time >= 4 and time < 8):
            print("Effect2")
        elif(time >= 8 and time < 10 ):
            print("effect 3")
        else:
            return True

        return False

Back2Basic.run()