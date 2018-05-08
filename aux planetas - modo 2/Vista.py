# coding=utf-8
"""
Clase Vista, crea ventana, llama a controlador y a los modelos
"""

# Importación de librerías
import os
import pygame

# Constantes
FPS = 60.0  # Cuántos cuadros se generan por cada segundo
PANTALLA_ALTO = 600
PANTALLA_ANCHO = 800

DT = 1.0 / FPS  # Cuánto tiempo real pasa entre cada cuadro


class Vista(object):
    """
    Clase vista, crea ventana
    """

    def __init__(self, modelo):
        """
        Constructor
        :param modelo: Universo de objetos
        :type modelo: Modelos
        """

        # Inicia pygame
        pygame.init()
        os.environ['SDL_VIDEO_CENTERED'] = '1'  # Ventana centrada al iniciarse

        # Crea la superficie de dibujado
        self._surface = pygame.display.set_mode((PANTALLA_ANCHO, PANTALLA_ALTO))

        # Temporizador
        self._clock = pygame.time.Clock()
        self._t = 0.0  # Tiempo de simulación
        self._dt = DT  # Dt variable, puede ser 0 ó DT dependiendo del input del usuario
        self._pausado = False  # Indica si se pausa o no la aplicación

        # Guarda M, C
        self._modelo = modelo

    def pausar(self):
        """
        Pausa o continúa la ejecución de la aplicación
        :return:
        """
        self._pausado = not self._pausado  # True->False, False->True
        if self._pausado:
            self._dt = 0
        else:
            self._dt = DT

    def dibujar(self):
        """
        Dibuja la aplicación
        :return:
        """

        # Ajusta reloj
        self._clock.tick(FPS)

        # Cambia el título
        pygame.display.set_caption('Simulador planetitas (FPS={0})'.format(int(self._clock.get_fps())))

        # Actualiza el modelo con el tiempo de la aplicación
        self._modelo.actualizar_posiciones(self._dt)

        # Dibuja el modelo
        self._modelo.dibujar_universo(self._surface)
        self._modelo.dibujar_trayectorias(self._surface)
        self._modelo.dibujar_planetas(self._surface)

        # Vuelca en pantalla
        pygame.display.flip()

        # Actualiza tiempo de la aplicación
        self._t += self._dt
