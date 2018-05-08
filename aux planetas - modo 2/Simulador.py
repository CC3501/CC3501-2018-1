# coding=utf-8
"""
Simulador, versión 2
Aplica concepto y separa claramente entre vista, modelo y controlador
"""

"""
Importación de objetos
"""
from Modelo import Modelos
from Vista import Vista
from Controlador import Controlador

"""
Crea los objetos
"""
modelo = Modelos()  # Crea un contenedor de modelos (Universo)
vista = Vista(modelo)  # Crea la vista
controlador = Controlador(modelo, vista)  # Crea el controlador de la aplicación

"""
Bucle de la aplicación
"""
while True:
    controlador.chequear_input()
    vista.dibujar()
