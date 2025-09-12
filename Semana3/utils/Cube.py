from OpenGL.GL import *

vertices = [(0.5, -0.5, 0.5), # coordenada 0
            (-0.5, -0.5, 0.5), # coordenada 1
            (0.5, 0.5, 0.5), # coordenada 2...
            (-0.5, 0.5, 0.5),
            (0.5, 0.5, -0.5),
            (-0.5, 0.5, -0.5),
            (0.5, -0.5, -0.5),
            (-0.5, -0.5, -0.5),
            (0.5, 0.5, 0.5),
            (-0.5, 0.5, 0.5),
            (0.5, 0.5, -0.5),
            (-0.5, 0.5, -0.5),
            (0.5, -0.5, -0.5),
            (0.5, -0.5, 0.5),
            (-0.5, -0.5, 0.5),
            (-0.5, -0.5, -0.5),
            (-0.5, -0.5, 0.5),
            (-0.5, 0.5, 0.5),
            (-0.5, 0.5, -0.5),
            (-0.5, -0.5, -0.5),
            (0.5, -0.5, -0.5),
            (0.5, 0.5, -0.5),
            (0.5, 0.5, 0.5),
            (0.5, -0.5, 0.5)
            ]
triangles = [0, 2, 3, 0, 3, 1, 8, 4, 5, 8, 5, 9, 10, 6, 7, 10, 7, 11, 12,
             13, 14, 12, 14, 15, 16, 17, 18, 16, 18, 19, 20, 21, 22, 20, 22, 23]

def wireCube():
    for t in range(len(triangles) - 3):
        glBegin(GL_LINES) # crear una línea
        glVertex3fv(vertices[triangles[t]]) # conecto el punto A
        glVertex3fv(vertices[triangles[t + 1]]) # conecto el punto B
        glVertex3fv(vertices[triangles[t + 2]]) # conecto el punto C
        glEnd() # finalizo la creación
        t += 3