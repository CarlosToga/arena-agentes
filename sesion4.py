# Sesión 4
# Agente con movimiento, rebote y rotación dinámica controlada con teclado

import pygame
import sys
import math

pygame.init()

ANCHO = 800
ALTO = 600

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Sesion 4 - Movimiento y Rotacion Controlada")

clock = pygame.time.Clock()


def rotar_punto(px, py, angulo):
    rad = math.radians(angulo)

    rx = math.cos(rad) * px - math.sin(rad) * py
    ry = math.sin(rad) * px + math.cos(rad) * py

    return rx, ry


class Agente:

    def __init__(self, x, y, tamano=40):

        self.x = x
        self.y = y

        self.vel_x = 3
        self.vel_y = 2

        self.tamano = tamano

        self.angulo = 0

        # vertices locales (triangulo)
        self.vertices_locales = [
            (0, -tamano),
            (-tamano // 2, tamano // 2),
            (tamano // 2, tamano // 2)
        ]

    def mover(self):

        self.x += self.vel_x
        self.y += self.vel_y

        # rebote en bordes
        if self.x < 0 or self.x > ANCHO:
            self.vel_x *= -1

        if self.y < 0 or self.y > ALTO:
            self.vel_y *= -1

    def rotar(self, direccion):

        velocidad_rotacion = 3

        if direccion == "izquierda":
            self.angulo -= velocidad_rotacion

        if direccion == "derecha":
            self.angulo += velocidad_rotacion

    def dibujar(self, superficie):

        vertices_globales = []

        for vx, vy in self.vertices_locales:

            rx, ry = rotar_punto(vx, vy, self.angulo)

            gx = self.x + rx
            gy = self.y + ry

            vertices_globales.append((gx, gy))

        pygame.draw.polygon(superficie, (0, 200, 255), vertices_globales)

        pygame.draw.circle(superficie, (255, 100, 100), (int(self.x), int(self.y)), 4)


agente = Agente(400, 300)


corriendo = True

while corriendo:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            corriendo = False

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        agente.rotar("izquierda")

    if teclas[pygame.K_RIGHT]:
        agente.rotar("derecha")

    agente.mover()

    pantalla.fill((0, 0, 0))

    agente.dibujar(pantalla)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()


