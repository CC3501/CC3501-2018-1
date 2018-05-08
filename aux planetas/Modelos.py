# coding=utf-8
"""
Clase Planeta, almacena propiedades del planeta
"""

# Importa clases
import math
import random
import pygame

# Colores
COLOR_BLANCO = (255, 255, 255)


class Planeta(object):
    """
    Planeta, tiene velocidad y radio de giro
    """

    def __init__(self, w=0, rplaneta=0, rgiro=0, thetai=0, colorplaneta=COLOR_BLANCO):
        """
        Constructor
        :param w: Velocidad angular
        :param rplaneta: Radio del planeta
        :param rgiro: Radio de giro (unidades con respecto a tamaño de pantalla)
        :param thetai: Posicion inicial en angulos (0,360)
        :param colorplaneta: Color del planeta
        """

        # Guarda las variables
        self._velocidad_angular = w
        self._radio_planeta = int(rplaneta)  # No se pueden dibujar radios tipo 3.4, no existen 3.4 pixeles
        self._radio_giro = rgiro
        self._theta = thetai
        self._color = colorplaneta

        # Calcula la posicion absoluta (con respecto a 0,0) y la guarda como propiedad del objeto
        self._posicion_absoluta = [0, 0]  # (x,y)

        # Posición del origen, sólo se puede cambiar una vez se crea el planeta
        self._pos_origen = [0, 0]

        # Actualiza la posición en t=0
        self.actualizar_posicion(0)

    # noinspection PyTypeChecker
    def actualizar_posicion(self, dt):
        """
        Actualiza la posición en un tiempo dt
        :return:
        """

        # Actualiza el ángulo
        self._theta += self._velocidad_angular * dt

        # Pasa a radianes
        theta_rad = self._theta * math.pi / 180

        # Calcula el par (x,y) de la posición
        x = self._radio_giro * math.cos(theta_rad)
        y = self._radio_giro * math.sin(theta_rad)

        # Guarda la posición
        self._posicion_absoluta[0] = x
        self._posicion_absoluta[1] = y

    def definir_origen(self, x, y):
        """
        Define el origen del planeta
        :param x: Coordenadas del origen, eje x
        :param y: Coordenadas del origen, eje y
        :return:
        """
        self._pos_origen[0] = int(x)
        self._pos_origen[1] = int(y)

    def obtener_origen(self):
        """
        Retorna origen del planeta
        :return: list
        """
        return self._pos_origen

    def obtener_posicion(self):
        """
        Retorna la posición absoluta del planeta en el tiempo actual
        :return: list
        """
        return self._posicion_absoluta

    def dibujar(self, surface):
        """
        Dibuja el Planeta en un canvas
        :param surface: Superficie de Pygame
        :return:
        """

        # Calcula la posición relativa al centro
        x_r = self._pos_origen[0] + self._posicion_absoluta[0]
        y_r = self._pos_origen[1] + self._posicion_absoluta[1]

        # Muy importante, pasar coordenadas a entero
        x_r = int(x_r)
        y_r = int(y_r)

        # circle(Surface, color, pos, radius, width=0) -> Rect
        pygame.draw.circle(surface, self._color, [x_r, y_r], self._radio_planeta)


def generar_planeta_aleatorio(wlims, rplanetalim, rgirolim):
    """
    Genera un planeta aleatorio
    :param wlims: Límites velocidad de giro
    :param rplanetalim: Límites del radio del planeta
    :param rgirolim: Límites radio de giro del planeta
    :return: Planeta
    """

    # Aleatoriza los parámetros multiplicándolos por un valor entre [0,1]
    w = random.randint(*wlims)
    rplaneta = random.randint(*rplanetalim)
    rgiro = random.randint(*rgirolim)
    thetai = random.randint(0, 360)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Retorna un planeta nuevo
    return Planeta(w=w, rplaneta=rplaneta, rgiro=rgiro, thetai=thetai, colorplaneta=color)
