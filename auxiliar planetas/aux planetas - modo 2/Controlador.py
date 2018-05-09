# coding=utf-8
"""
Clase controlador, recibe puntero al sistema de objetos (Universo) y los modifica según input del usuario
"""

# Importación de librerías
import pygame
from pygame.locals import *


class Controlador(object):
    """
    Revisa el input del usuario y hace cambios en modelo (crear más planetas) o ventana (cerrar)
    """

    def __init__(self, modelos, vista):
        """
        Constructor
        :param modelos: Objeto de universo
        :param vista: Objeto de vista
        """
        self._modelos = modelos
        self._vista = vista

    def chequear_input(self):
        """
        Chequea el input del usuario
        :return:
        """
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:  # Al teclear Enter se añade un planeta aleatorio
                    self._modelos.agregar_planeta_aleatorio()
                elif event.key == K_SPACE:  # Al teclear espacio se pausa o continúa
                    self._vista.pausar()
