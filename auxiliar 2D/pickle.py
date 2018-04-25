from CC3501Utils import *


class Pickle(Figura):
    def __init__(self, pos=Vector(0, 0), rgb=(1.0, 1.0, 1.0)):
        super().__init__(pos, rgb)

    def figura(self):

        glBegin(GL_QUADS)

        glColor3f(11/255, 76/255, 25/255)
        #Medio
        glVertex2f(0, 100)
        glVertex2f(50, 100)
        glVertex2f(50, 0)
        glVertex2f(0, 0)
        glEnd()

        # arriba
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(25, 100)
        radio = 25
        ang = pi / 10
        for i in range(11):
            ang_i = ang * i
            glVertex(25 + cos(ang_i) * radio, 100 + sin(ang_i) * radio)

        glEnd()
        #abajo
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(25, 0)
        radio = 25
        ang = pi/10
        for i in range(11):
            ang_i = -ang*i
            glVertex(25+cos(ang_i)*radio, sin(ang_i)*radio)

        glEnd()

        # ojos
        glColor3f(1.0, 1.0, 1.0)
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(10, 100)
        radio = 5
        ang = 2*pi / 10
        for i in range(11):
            ang_i = ang * i
            glVertex(10 + cos(ang_i) * radio, 100 + sin(ang_i) * radio)

        glEnd()

        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(30, 100)
        radio = 5
        ang = 2 * pi / 10
        for i in range(11):
            ang_i = ang * i
            glVertex(30 + cos(ang_i) * radio, 100 + sin(ang_i) * radio)

        glEnd()




