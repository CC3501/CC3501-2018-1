#####################################################################
# Mauricio Araneda H.
# CC3501
#####################################################################

# Ejemplo.py
# ---------------
# Ejemplo para aux
# ---------------

# Implementación testeada con:
## Python 3.5
## PyOpenGL 3.1.0
## PyGame 1.9.3
#####################################################################
import os
import random
from CC3501Utils import *
from vista import *
from morty import *
from pickle import *
#####################################################################

os.environ['SDL_VIDEO_CENTERED'] = '1'  # centrar pantalla

def main():
    ancho = 800
    alto = 600
    init(ancho, alto, "Ejemplo Aux")
    vista = Vista()

    pjs = []
    morty = Morty(Vector(100, 100))
    pjs.append(morty)
    pjs.append(Pickle(Vector(400,300)))

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == QUIT:  # cerrar ventana
                run = False

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pass

                if event.key == K_RIGHT:
                    morty.pos += Vector(10, 0)
                if event.key == K_LEFT:
                    morty.pos -= Vector(10, 0)
                if event.key == K_UP:
                    morty.pos += Vector(0, 10)
                if event.key == K_DOWN:
                    morty.pos -= Vector(0, 10)

        vista.dibujar(pjs)

        pygame.display.flip()  # actualizar pantalla
        pygame.time.wait(int(1000 / 30))  # ajusta a 30 fps

    pygame.quit()

main()