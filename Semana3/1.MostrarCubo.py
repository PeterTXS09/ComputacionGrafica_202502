import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from utils.Cube import wireCube

pygame.init()

# configuración del proyecto
screen_width = 1000
screen_height = 800
background_color = (0, 0, 0, 1)
drawing_color = (1, 1, 1, 1)

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL en Python')

# variables de transformación
rotation = [0, 0, 0]   # ángulos de rotación en X, Y, Z
translation = [0, 0, -5]  # posición del objeto (X, Y, Z)
scale = 1.0  # factor de escala

# velocidades
translation_speed = 0.05
rotation_speed = 2
scale_speed = 0.02


def initialise():
    glClearColor(background_color[0], background_color[1], background_color[2], background_color[3])
    glColor(drawing_color)

    # projection
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (screen_width / screen_height), 0.1, 100.0)

    # modelview
    glMatrixMode(GL_MODELVIEW)
    glTranslate(0, 0, 0)
    glLoadIdentity()
    glViewport(0, 0, screen.get_width(), screen.get_height())
    glEnable(GL_DEPTH_TEST)
    glTranslate(0, 0, -2)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # glRotatef(1, 10, 0, 1)
    glPushMatrix()

    # aplicar transformaciones en orden: traslación -> rotación -> escala
    glTranslatef(*translation)  # mover el cubo
    glRotatef(rotation[0], 1, 0, 0)  # rotar en eje X
    glRotatef(rotation[1], 0, 1, 0)  # rotar en eje Y
    glRotatef(rotation[2], 0, 0, 1)  # rotar en eje Z
    glScalef(scale, scale, scale)  # escalar uniformemente

    wireCube()
    glPopMatrix()


done = False
clock = pygame.time.Clock()
initialise()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    keys = pygame.key.get_pressed()
    # traslación
    if keys[K_w]: translation[1] += translation_speed
    if keys[K_s]: translation[1] -= translation_speed
    if keys[K_a]: translation[0] -= translation_speed
    if keys[K_d]: translation[0] += translation_speed
    if keys[K_q]: translation[2] += translation_speed
    if keys[K_e]: translation[2] -= translation_speed

    # rotación
    if keys[K_LEFT]:  rotation[1] -= rotation_speed
    if keys[K_RIGHT]: rotation[1] += rotation_speed
    if keys[K_UP]:    rotation[0] -= rotation_speed
    if keys[K_DOWN]:  rotation[0] += rotation_speed
    if keys[K_z]:     rotation[2] += rotation_speed
    if keys[K_x]:     rotation[2] -= rotation_speed

    # escala
    if keys[K_PLUS] or keys[K_EQUALS]: scale += scale_speed
    if keys[K_MINUS]: scale = max(0.1, scale - scale_speed)

    display()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()