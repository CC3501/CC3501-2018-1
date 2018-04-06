# coding=utf-8
"""
Esto hace tarea
@author pablo
@version 1.1
"""

# Importar librería
import matplotlib.pyplot as plt  # grafico
import math
import numpy as np


# noinspection PyBroadException
class Rio:
    def __init__(self, ancho, largo, dh, tol):
        """
        Constructor
        :param ancho: Ancho
        :param largo: Largo
        :param dh: Tamaño grilla diferencial
        :param tol: Tolerancia
        :type ancho: int,float
        """

        # Configuraciones de dimensiones
        self._ancho = ancho
        self._largo = largo
        self._dh = dh
        self._h = int(float(ancho) / dh)
        self._w = int(float(largo) / dh)

        # Matriz
        self._matrix = np.ones((self._h, self._w))

        # Define la tolerancia
        self.tol = tol

        # Indica última condición de borde usada
        self._lastcb = 0

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
        self._lastcb = t
        for i in range(self._h):
            self._matrix[i][0] = 5 * t + 4 * i

    def reset(self):
        """
        Resetea la matriz
        :return:
        """
        self._matrix = np.ones((self._h, self._w))
        self.cb(self._lastcb)

    def _single_iteration(self, matrix_new, matrix_old, omega):
        """
        Inicia calculo sólo 1 iteración
        :return:
        """
        for x in range(1, self._w):
            for y in range(self._h):

                # Valor anterior de la matriz promediado
                prom = 0

                # General
                if 1 < y < self._h - 2 and x < self._w - 2:
                    prom = 0.25 * (matrix_old[y - 1][x] + matrix_old[y + 1][x] + matrix_old[y][x - 1] +
                                   matrix_old[y][x + 1] - 4 * matrix_old[y][x])

                # Borde superior
                if y == 0 and x < self._w - 2:
                    prom = 0.25 * (2 * matrix_old[y + 1][x] + matrix_old[y][x - 1] +
                                   matrix_old[y][x + 1] - 4 * matrix_old[y][x])

                # Borde inferior
                if y == self._h - 1 and x < self._w - 2:
                    prom = 0.25 * (2 * matrix_old[y - 1][x] + matrix_old[y][x - 1] + matrix_old[y][x + 1] - 4 *
                                   matrix_old[y][x])

                # Borde superior derecho
                if y == 0 and x == self._w - 1:
                    prom = 0.25 * (2 * matrix_old[y + 1][x] + 2 * matrix_old[y][x - 1] - 4 * matrix_old[y][x])

                # Borde inferior derecho
                if y == self._h - 1 and x == self._w - 1:
                    prom = 0.25 * (2 * matrix_old[y - 1][x] + 2 * matrix_old[y][x - 1] - 4 * matrix_old[y][x])

                # Calcula nuevo valor
                matrix_new[y][x] = matrix_old[y][x] + prom * omega

    @staticmethod
    def _convergio(mat_old, mat_new, tol):
        """
        Retorna un booleano indicando si el problema convergió o no.

        :param mat_old: Vector de soluciones previo
        :param mat_new: Vector de soluciones posterior
        :param tol: Error máximo admisible
        :return:
        """
        not_zero = (mat_new != 0)
        diff_relativa = (mat_old - mat_new)[not_zero]
        max_diff = np.max(np.fabs(diff_relativa))
        return [max_diff < tol, max_diff]

    def start(self, omega):
        """
        Soluciona el sistema
        :return:
        """

        # Clonamos las matrices
        mat_new = np.copy(self._matrix)

        # Inicia variables
        niters = 0
        run = True
        converg = []
        omega = omega - 1
        if not 0 <= omega <= 1:
            raise Exception('Omega tiene un valor incorrecto')

        while run:
            mat_old = np.copy(mat_new)
            self._single_iteration(mat_new, mat_old, omega)
            niters += 1
            converg = self._convergio(mat_old, mat_new, self.tol)
            run = not converg[0]

        print 'El programa terminó en {0} iteraciones, con error {1}'.format(niters, converg[1])
        self._matrix = np.copy(mat_new)
        return niters

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

    def w_optimo(self):
        """
        Retorna el w optimo
        :return:
        """

        def createw(n, m):
            return 4 / (2 + (math.sqrt(4 - (math.cos(math.pi / (n - 1)) + math.cos(math.pi / (m - 1))) ** 2)))

        return createw(self._w, self._h)


# Instancia rio
r = Rio(3, 7, 0.1, 0.1)
r.cb(10)

# Se prueban varios w
omegas = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
iters = []
errors = []
for w in omegas:
    iters.append(r.start(w))
    r.reset()
r.plot()

# Graficamos variación de iteraciones
plt.plot(omegas, iters)
plt.xlabel('Omega')
plt.ylabel('Numero de iteraciones')
plt.show()
