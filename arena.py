import pygame
import sys
import numpy as np

print("¡Todo instalado correctamente!")
print("NumPy versión:", np.__version__)
print("Pygame versión:", pygame.__version__)

pygame.init()
pantalla = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Prueba de instalación")

corriendo = True

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    pantalla.fill((0, 0, 0))
    pygame.draw.circle(pantalla, (255, 0, 0), (200, 150), 50)
    pygame.display.flip()

pygame.quit()
sys.exit()