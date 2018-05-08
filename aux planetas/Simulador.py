# coding=utf-8
"""
Simulador, ventana gráfica en la cual
1) Se inician los planetas -> Modelo
2) Se crea la vista, pantalla -> Vista
3) Se recoge input de usuario -> Controlador
"""

"""
Importación de librerías
"""

# Importa pygame
import pygame
from pygame.locals import *

# Importa los objetos
from Modelos import Planeta, generar_planeta_aleatorio

# Importa otras librerías adicionales
import os

"""
Constantes de la aplicación
"""
COLOR_FONDO = (0, 0, 0)  # Negro
FPS = 60.0  # Cuántos cuadros se generan por cada segundo
PANTALLA_ALTO = 600
PANTALLA_ANCHO = 800

"""
Crea la ventana
"""
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'  # Ventana centrada al iniciarse

surface = pygame.display.set_mode((PANTALLA_ANCHO, PANTALLA_ALTO))

"""
Crea el reloj de la aplicación
"""
clock = pygame.time.Clock()
dt = 1.0 / FPS  # Cuánto tiempo real pasa entre cada cuadro
t = 0.0  # Tiempo de simulación

"""
Objetos del modelo, arreglo de planetas
"""
planetas = []

# Crea un sol y lo añade a los planetas
sol = Planeta(rplaneta=50, imagenplaneta='imagenes/sol.png')  # Color amarillo
sol.definir_origen(PANTALLA_ANCHO / 2, PANTALLA_ALTO / 2)  # El sol está centrado
planetas.append(sol)

"""
Bucle de la aplicación
"""
while True:

    # Nuevo cuadro
    clock.tick(FPS)

    pygame.display.set_caption('Simulador planetitas (FPS={0})'.format(int(clock.get_fps())))

    # Pinta la superficie
    surface.fill(COLOR_FONDO)

    """
    Controlador
    """
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_RETURN:  # Al teclear Enter se añade un planeta aleatorio

                nuevo_planeta = generar_planeta_aleatorio(wlims=[50, 90],
                                                          rplanetalim=[10, 30],
                                                          rgirolim=[80, PANTALLA_ANCHO / 2],
                                                          imgprob=1.0
                                                          )
                nuevo_planeta.definir_origen(*sol.obtener_origen())
                planetas.append(nuevo_planeta)

    """
    Se dibujan los planetas
    """
    for p in planetas:
        p.actualizar_posicion(dt)
        p.dibujar(surface)

    # Flip surface
    pygame.display.flip()

    # Incrementa el tiempo
    t += dt
