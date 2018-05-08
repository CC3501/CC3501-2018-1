# coding=utf-8
"""
Modelo, maneja todos los objetos de la aplicación
"""

# Importación de librerías
from Planetas import Planeta, generar_planeta_aleatorio
from Vista import PANTALLA_ALTO, PANTALLA_ANCHO


class Modelos(object):
    """
    Contiene planetas y revisa sus interacciones
    """

    def __init__(self):
        """
        Constructor
        """

        # Arreglo de planetas
        self._planetas = []

        # Crea un sol y lo añade a los planetas
        self._sol = Planeta(rplaneta=50, imagenplaneta='imagenes/sol.png')  # Color amarillo
        self._sol.definir_origen(PANTALLA_ANCHO / 2, PANTALLA_ALTO / 2)  # El sol está centrado
        self._planetas.append(self._sol)

        # Color de fondo del universo
        self._fondo_universo = (0, 0, 0)  # Negro

    def agregar_planeta_aleatorio(self):
        """
        Añade un planeta aleatorio
        :return:
        """
        nuevo_planeta = generar_planeta_aleatorio(wlims=[50, 150],
                                                  rplanetalim=[10, 30],
                                                  rgirolim=[80, PANTALLA_ANCHO / 2],
                                                  imgprob=1.0
                                                  )
        nuevo_planeta.definir_origen(*self._sol.obtener_origen())
        self._planetas.append(nuevo_planeta)

    def actualizar_posiciones(self, dt):
        """
        Actualiza las posiciones de los planetas
        :param dt: Incremento de tiempo
        :return:
        """
        for p in self._planetas:
            p.actualizar_posicion(dt)

    def dibujar_universo(self, surface):
        """
        Dibuja el universo en pantalla
        :param surface: Superficie de dibujo
        :return:
        """
        surface.fill(self._fondo_universo)

    def dibujar_trayectorias(self, surface):
        """
        Dibuja las trayectorias de los planetas
        :param surface: Superficie de dibujo
        :return:
        """
        for p in self._planetas:
            p.dibujar_trayectoria(surface)

    def dibujar_planetas(self, surface):
        """
        Dibuja los planetas con un cierto incremento del tiempo
        :param surface: Superficie de dibujo
        :return:
        """
        for p in self._planetas:
            p.dibujar_planeta(surface)
