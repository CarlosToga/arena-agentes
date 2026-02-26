import pygame
import sys
import math

pygame.init()

ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Sesión 2 - Agente con Rotación")

def rotar_punto(px, py, angulo_grados):
    """Rota un punto (px,py) alrededor del origen (0,0)"""
    rad = math.radians(angulo_grados)
    qx = math.cos(rad) * px - math.sin(rad) * py
    qy = math.sin(rad) * px + math.cos(rad) * py
    return qx, qy


class Agente:
    def __init__(self, x, y, tamano=40):
        """Inicializa el agente con posición, tamaño y ángulo"""
        self.x = x
        self.y = y
        self.tamano = tamano
        self.angulo = 30  # ángulo inicial diferente de 0

        # Triángulo simétrico apuntando hacia arriba
        self.vertices_locales = [
            (0, -tamano),
            (-tamano // 2, tamano // 2),
            (tamano // 2, tamano // 2)
        ]

    def dibujar(self, superficie):
        """Dibuja el agente aplicando rotación alrededor de su centro"""
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

    pantalla.fill((0, 0, 0))
        # -------- Ejercicio 1: Puntos --------
    pygame.draw.circle(pantalla, (255, 255, 255), (100, 100), 5)
    pygame.draw.circle(pantalla, (255, 0, 0), (200, 300), 8)
    pygame.draw.circle(pantalla, (0, 255, 0), (400, 150), 6)
    pygame.draw.circle(pantalla, (0, 0, 255), (600, 400), 7)

    # -------- Ejercicio 2: Líneas --------
    pygame.draw.line(pantalla, (200, 200, 200), (100, 100), (200, 300), 3)
    pygame.draw.line(pantalla, (100, 255, 100), (200, 300), (400, 150), 5)

    # -------- Ejercicio 3: Polígonos --------
    pygame.draw.polygon(pantalla, (255, 255, 0),
                        [(300, 100), (350, 200), (250, 200)])

    pygame.draw.polygon(pantalla, (255, 255, 255),
                        [(500, 300), (600, 450), (400, 450)], width=4)
    agente.dibujar(pantalla)
    pygame.display.flip()

pygame.quit()
sys.exit()