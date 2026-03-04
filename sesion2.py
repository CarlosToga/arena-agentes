import pygame
import sys
import math

pygame.init()

ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Sesión 3 - Agente con Movimiento y Rotación")


def rotar_punto(px, py, angulo_grados):
    """Rota un punto (px,py) alrededor del origen (0,0)"""
    rad = math.radians(angulo_grados)
    qx = math.cos(rad) * px - math.sin(rad) * py
    qy = math.sin(rad) * px + math.cos(rad) * py
    return qx, qy


class Agente:
    def __init__(self, x, y, tamano=40):
        """Inicializa el agente con posición, tamaño, ángulo y velocidad"""
        self.x = x
        self.y = y
        self.tamano = tamano
        self.angulo = 30  # Ángulo inicial diferente de 0

        # Velocidad
        self.vel_x = 3
        self.vel_y = 2

        # Triángulo simétrico centrado en (0,0)
        self.vertices_locales = [
            (0, -tamano),
            (-tamano // 2, tamano // 2),
            (tamano // 2, tamano // 2)
        ]

    def mover(self):
        """Actualiza posición y aplica rebote en los límites"""
        self.x += self.vel_x
        self.y += self.vel_y

        # Rebote horizontal
        if self.x > ANCHO - self.tamano or self.x < self.tamano:
            self.vel_x *= -1

        # Rebote vertical
        if self.y > ALTO - self.tamano or self.y < self.tamano:
            self.vel_y *= -1

    def dibujar(self, superficie):
        """Dibuja el agente aplicando rotación y traslación"""
        vertices_globales = []

        for vx, vy in self.vertices_locales:
            # Rotación
            rx, ry = rotar_punto(vx, vy, self.angulo)

            # Traslación
            gx = self.x + rx
            gy = self.y + ry

            vertices_globales.append((gx, gy))

        pygame.draw.polygon(superficie, (0, 200, 255), vertices_globales)
        pygame.draw.circle(superficie, (255, 100, 100), (int(self.x), int(self.y)), 4)


agente = Agente(400, 300)

reloj = pygame.time.Clock()
corriendo = True

while corriendo:
    reloj.tick(60)  # 60 FPS

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    pantalla.fill((0, 0, 0))

    # Movimiento del agente
    agente.mover()

    # Dibujo del agente
    agente.dibujar(pantalla)

    pygame.display.flip()

pygame.quit()
sys.exit()