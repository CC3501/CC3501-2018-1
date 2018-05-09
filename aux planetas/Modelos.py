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
COLOR_TRAYECTORIA = (50, 50, 50)


class Planeta(object):
    """
    Planeta, tiene velocidad y radio de giro
    """

    def __init__(self, w=0, rplaneta=0, rgiro=0, thetai=0, colorplaneta=COLOR_BLANCO, imagenplaneta=''):
        """
        Constructor
        :param w: Velocidad angular
        :param rplaneta: Radio del planeta
        :param rgiro: Radio de giro (unidades con respecto a tamaño de pantalla)
        :param thetai: Posicion inicial en angulos (0,360)
        :param colorplaneta: Color del planeta
        """

        # Verifica que las variables tengan sentido
        assert rplaneta != 0, 'El radio del planeta no puede ser cero'
        if rgiro != 0: #sol
            assert rgiro > rplaneta, 'El radio de giro no puede ser menor que el radio del planeta'

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

        # Si se pasa una imagen como argumento se carga, si no se define como None
        if imagenplaneta == '':
            self._img = None
        else:
            # Carga la imagen, retorna surface
            self._img = pygame.image.load(imagenplaneta)

            # Escala la superficie al tamaño del radio de giro
            self._img = pygame.transform.scale(self._img, [self._radio_planeta * 2, self._radio_planeta * 2])

    # noinspection PyTypeChecker
    def actualizar_posicion(self, dt):
        """
        Actualiza la posición en un tiempo dt
        :return:
        """

        # Actualiza el ángulo
        self._theta += self._velocidad_angular * dt
        self._theta %= 360

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

    def dibujar_trayectoria(self, surface):
        """
        Dibuja la trayectoria del planeta
        :param surface:
        :return:
        """
        if self._radio_giro > 0:
            pygame.draw.circle(surface, COLOR_TRAYECTORIA, self._pos_origen, self._radio_giro, 1)

    def dibujar_planeta(self, surface):
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

        # Si se definió una imagen se dibuja
        if self._img is not None:
            # Se resta el radio para centrar
            surface.blit(self._img, [x_r - self._radio_planeta, y_r - self._radio_planeta])
        else:
            # circle(Surface, color, pos, radius, width=0) -> Rect
            pygame.draw.circle(surface, self._color, [x_r, y_r], self._radio_planeta)


def generar_planeta_aleatorio(wlims, rplanetalim, rgirolim, imgprob=0.5):
    """
    Genera un planeta aleatorio
    :param wlims: Límites velocidad de giro
    :param rplanetalim: Límites del radio del planeta
    :param rgirolim: Límites radio de giro del planeta
    :param imgprob: Probabilidad de cargar imagen en el planeta
    :return: Planeta
    """

    # Aleatoriza los parámetros multiplicándolos por un valor entre [0,1]
    w = random.randint(*wlims)
    rplaneta = random.randint(*rplanetalim)
    rgiro = random.randint(*rgirolim)
    thetai = random.randint(0, 360)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Se carga imagen según probabilidad
    if random.random() <= imgprob:
        img = 'imagenes/planeta{0}.png'.format(random.randint(1, 10))
    else:
        img = ''

    # Retorna un planeta nuevo
    return Planeta(w=w,
                   rplaneta=rplaneta,
                   rgiro=rgiro,
                   thetai=thetai,
                   colorplaneta=color,
                   imagenplaneta=img
                   )
