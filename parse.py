from display import *
from matrix import *
from draw import *



def parse(name, edges, triangles, cs, s, c, zbuffer):
    f = open(name)
    lines = f.readlines()
    i = 0
    while i < len(lines):
        if lines[i] == "pop\n":
            cs.pop()
        if lines[i] == "push\n":
            m = list(cs[-1])
            cs.append(m)
        if lines[i] == "line\n":
            k = lines[i+1].split()
            add_edge(edges, [float(k[0]), float(k[1]), float(k[2])], [float(k[3]), float(k[4]), float(k[5])])
            edges = matrix_multiply(cs[-1], edges)
            draw_2D_edges(edges, s, c)
            edges = [[], [], [], []]
            i += 1
        elif lines[i] == "circle\n":
            k = lines[i+1].split()
            add_circle(edges, float(k[0]), float(k[1]), float(k[2]), float(k[3]), 0.01)
            edges = matrix_multiply(cs[-1], edges)
            draw_2D_edges(edges, s, c)
            edges = [[], [], [], []]
            i += 1
        elif lines[i] == "hermite\n":
            k = lines[i+1].split()
            add_hermite(edges, float(k[0]), float(k[1]), float(k[2]), float(k[3]), float(k[4]), float(k[5]), float(k[6]), float(k[7]), 0.01)
            edges = matrix_multiply(cs[-1], edges)
            draw_2D_edges(edges, s, c)
            edges = [[], [], [], []]
            i == 1
        elif lines[i] == "bezier\n":
            k = lines[i+1].split()
            add_bezier(edges, float(k[0]), float(k[1]), float(k[2]), float(k[3]), float(k[4]), float(k[5]), float(k[6]), float(k[7]), 0.01)
            edges = matrix_multiply(cs[-1], edges)
            draw_2D_edges(edges, s, c)
            edges = [[], [], [], []]
            i += 1
        elif lines[i] == "box\n":
            k = lines[i+1].split()
            add_box(triangles, float(k[0]), float(k[1]), float(k[2]), float(k[3]), float(k[4]), float(k[5]))
            triangles = matrix_multiply(cs[-1], triangles)
            draw_3D_triangles(triangles, s, c, zbuffer)
            triangles = [[], [], [], []]
            i += 1
        elif lines[i] == "sphere\n":
            k = lines[i+1].split()
            add_sphere(triangles, float(k[0]), float(k[1]), float(k[2]), float(k[3]), 0.05)
            triangles = matrix_multiply(cs[-1], triangles)
            draw_3D_triangles(triangles, s, c, zbuffer)
            triangles = [[], [], [], []]
            i += 1
        elif lines[i] == "torus\n":
            k = lines[i+1].split()
            add_torus(triangles, float(k[0]), float(k[1]), float(k[2]), float(k[3]), float(k[4]), 0.05)
            triangles = matrix_multiply(cs[-1], triangles)
            draw_3D_triangles(triangles, s, c, zbuffer)
            triangles = [[], [], [], []]
            i += 1
        elif lines[i] == "scale\n":
            k = lines[i+1].split(" ")
            m = scale(float(k[0]), float(k[1]), float(k[2]))
            cs[-1] = matrix_multiply(cs[-1], m)
            i += 1
        elif lines[i] == "move\n":
            k = lines[i+1].split(" ")
            m = translate(float(k[0]), float(k[1]), float(k[2]))
            cs[-1] = matrix_multiply(cs[-1], m)
            i += 1
        elif lines[i] == "rotate\n":
            k = lines[i+1].split(" ")
            if k[0] == "x":
                m = rotatex(float(k[1]))
            elif k[0] == "y":
                m = rotatey(float(k[1]))
            elif k[0] == "z":
                m = rotatez(float(k[1]))
            cs[-1] = matrix_multiply(cs[-1], m)
            i += 1
        elif lines[i] == "display\n":
            display(s)
        elif lines[i] == "save\n":
            save_extension(s, lines[i+1].strip())
        i += 1
