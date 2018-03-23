# coding=utf-8
"""
Esto hace tarea
@author pablo
@version 1.1
"""

# Importar librería
import matplotlib.pyplot as plt  # grafico
import tqdm
import numpy as np


class Rio:
    def __init__(self, ancho, largo, dh):
        """
        Constructor
        :param ancho: Ancho
        :param largo: Largo
        :param dh: Tamaño grilla diferencial
        :type ancho: int,float
        """
        self._ancho = ancho  # privada
        self._largo = largo
        self._dh = dh

        self._h = int(float(ancho) / dh)
        self._w = int(float(largo) / dh)

        self._matrix = np.ones((self._h, self._w))

    def imprime(self):
        """
        Imprime el rio
        :return:
        """
        print(self._matrix)

    def cb(self, t):
        """
        Pone cond borde
        :param t: Tiempo
        :return:
        """
        for i in range(self._h):
            self._matrix[i][0] = 5 * t + 4 * i

    def start(self):
        """
        Inicia calculo
        :return:
        """
        for _ in tqdm.tqdm(range(1000)):
            for x in range(1, self._w):
                for y in range(self._h):

                    # General
                    if 1 < y < self._h - 2 and x < self._w - 2:
                        self._matrix[y][x] = 0.25 * (
                                self._matrix[y - 1][x] + self._matrix[y + 1][x] + self._matrix[y][x - 1] +
                                self._matrix[y][x + 1])

                    # Borde superior
                    if y == 0 and x < self._w - 2:
                        self._matrix[y][x] = 0.25 * (
                                2 * self._matrix[y + 1][x] + self._matrix[y][x - 1] +
                                self._matrix[y][x + 1])

                    # Borde inferior
                    if y == self._h - 1 and x < self._w - 2:
                        self._matrix[y][x] = 0.25 * (
                                2 * self._matrix[y - 1][x] + self._matrix[y][x - 1] +
                                self._matrix[y][x + 1])

                    # Borde superior derecho
                    if y == 0 and x == self._w - 1:
                        self._matrix[y][x] = 0.25 * (
                                2 * self._matrix[y + 1][x] + 2 * self._matrix[y][x - 1])

                    # Borde inferior derecho
                    if y == self._h - 1 and x == self._w - 1:
                        self._matrix[y][x] = 0.25 * (
                                2 * self._matrix[y - 1][x] + 2 * self._matrix[y][x - 1])

    def plot(self):
        """
        Grafica
        :return: None
        """
        fig = plt.figure()
        ax = fig.add_subplot(111)

        # Se agrega grafico al plot
        cax = ax.imshow(self._matrix, interpolation='none')
        fig.colorbar(cax)
        plt.show()


# Instancia rio
r = Rio(3, 7, 0.05)
r.cb(10)
r.start()
r.plot()
