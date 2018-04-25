from CC3501Utils import *


class Morty(Figura):
    def __init__(self, pos=Vector(0, 0), rgb=(1.0, 1.0, 1.0)):
        super().__init__(pos, rgb)

    def figura(self):

        glBegin(GL_QUADS)

        glColor3f(244/255, 232/255, 66/255)
        #Torso
        glVertex2f(0, 100)
        glVertex2f(50, 100)
        glVertex2f(50, 0)
        glVertex2f(0, 0)


        #Hombros
        glVertex2f(50, 100)
        glVertex2f(70, 100)
        glVertex2f(70, 70)
        glVertex2f(50, 70)

        glVertex2f(-20, 100)
        glVertex2f(0, 100)
        glVertex2f(0, 70)
        glVertex2f(-20, 70)


        #Brazos
        glColor3f(252/255, 193/255, 156/255)

        glVertex2f(50, 70)
        glVertex2f(65, 70)
        glVertex2f(65, 10)
        glVertex2f(50, 10)

        glVertex2f(-15, 70)
        glVertex2f(0, 70)
        glVertex2f(0, 10)
        glVertex2f(-15, 10)
        glEnd()

        # pelo
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(114 / 255, 61 / 255, 27 / 255)
        glVertex2f(25, 135)
        radio = 30
        ang = 2 * pi / 20
        for i in range(21):
            ang_i = ang * i
            glVertex(25 + cos(ang_i) * radio, 135 + sin(ang_i) * radio)

        glEnd()
        #cabeza
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(252 / 255, 193 / 255, 156 / 255)
        glVertex2f(25, 125)
        radio = 30
        ang = 2*pi/20
        for i in range(21):
            ang_i = ang*i
            glVertex(25+cos(ang_i)*radio, 125+sin(ang_i)*radio)

        glEnd()

        #Pantalones
        glColor3f(12/255, 8/255, 124/255)
        glBegin(GL_QUADS)

        glVertex2f(15, 0)
        glVertex2f(0, 0)
        glVertex2f(0, -50)
        glVertex2f(15, -50)

        glVertex2f(15, -20)
        glVertex2f(35, -20)
        glVertex2f(35, 0)
        glVertex2f(15, 0)

        glVertex2f(35, -50)
        glVertex2f(50, -50)
        glVertex2f(50,0)
        glVertex2f(35,0)

        glEnd()


