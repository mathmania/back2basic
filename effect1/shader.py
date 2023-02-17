def getShader(ctx):
    prog = ctx.program(
        vertex_shader='''
            #version 330

            in vec2 in_vert;
            in vec3 in_color;
            in float in_time;

            out vec3 v_color;
        
            void main() {
                v_color = vec3(0.3, 0.2, 0.6);
                
                float padded_x = round(in_vert.x * 10);
                if(mod(padded_x,3) != 0) {
                    gl_Position = vec4(in_vert.x, in_vert.y + sin(in_time * 0.5)*0.5, 0.0, 1.0);
                } else {
                    gl_Position = vec4(in_vert.x, in_vert.y - sin(in_time * 0.5)*0.5, 0.0, 1.0);
                }
            }
        ''',
        fragment_shader='''
            #version 330

            in vec2 in_vert;
            in vec3 v_color;
            in float v_time;

            out vec3 f_color;

            void main() {
                f_color = v_color;
            }
        ''',
    )

    return prog