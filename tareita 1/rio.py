# coding=utf-8
"""
Esto hace tarea
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

        self._matrix = np.zeros((self._h, self._w))
        self._rio = np.zeros((self._h, self._w))


        self._adh = int(float(1)/dh)

        #Test RIO
        self._contornos=[]
        self._cont_der=[]
        self._cont_izq=[]
        self._cont_inf=[]
        self._cont_sup=[]
        self._pilares = []

    def reset(self):
        """
        Retorna al rio a su estado inicial 
        """
        self.__init__(self._ancho,self._largo,self._dh)

    def imprime(self):
        """
        Imprime el rio
        :return:
        """
        print(self._matrix)

    def old_cb(self,t):
        """
        Pone cond borde
        :param t: Tiempo
        :return:
        """
        
        _t=5*t
        for i in range(self._h):
            self._matrix[i][0] = _t + 4 * i
        
        for (x,y) in self._cont_der:
            self._matrix[y][x] = 0
    
    
    def cb(self, t):
        """
        Pone cond borde
        :param t: Tiempo
        :return:
        """
    
        largo = len(self._matrix[:,0]) - 1 
        _t=5*t
        for i in range(self._h):
            if i <= largo/2:
                self._matrix[i][0] = _t + 5 * i
            elif i>=largo/2:
                self._matrix[i][0] = _t + 5 * abs(largo-i)
        
        for (x,y) in self._cont_der:
            self._matrix[y][x] = 0

    def start(self):
        """
        Inicia calculo
        :return:
        """

        for _ in tqdm.tqdm(range(1000)): #1000 iteraciones
            for x in range(1, self._w):
                for y in range(self._h):

                    # Borde superior
                    if y == 0 and x <= self._w - 2:
                        self._matrix[y][x] = 0.25 * (
                                2 * self._matrix[y + 1][x] + self._matrix[y][x - 1] + self._matrix[y][x + 1])

                    # Borde inferior
                    if y == self._h - 1 and x <= self._w - 2:
                        self._matrix[y][x] = 0.25 * (2 * self._matrix[y - 1][x] + self._matrix[y][x - 1] + self._matrix[y][x + 1])
                    
                    # Borde derecho #Final Rio                    
                    if x == self._w-1:
                        #superior derecho
                        if y == 0:
                            self._matrix[y][x] = 0.25 * (2 * self._matrix[y + 1][x] + 2 * self._matrix[y][x - 1])
                        # Borde inferior derecho
                        elif y == self._h - 1:
                            self._matrix[y][x] = 0.25 * (2 * self._matrix[y - 1][x] + 2 * self._matrix[y][x - 1])

                        # Borde derecho
                        else:
                            self._matrix[y][x] = 0.25 * (self._matrix[y + 1][x] + 2*self._matrix[y][x - 1] + self._matrix[y-1][x])

                    # Dentro rio
                    if 1 <= y <= self._h - 2 and x <= self._w - 2:

                        #Es el contorno derecho de un pillar
                        if (x,y) in self._cont_der:
                            continue
                        #Es el contorno izquierdo de un pilar                        
                        elif (x,y) in self._cont_izq:
                            self._matrix[y][x] = 0.25*(self._matrix[y + 1][x] + 2*self._matrix[y][x - 1] + self._matrix[y-1][x])
                        #Es el contorno superior de un pilar                        
                        elif (x,y) in self._cont_sup:
                            self._matrix[y][x] = 0.25 * (2 * self._matrix[y - 1][x] + self._matrix[y][x - 1] + self._matrix[y][x + 1])
                        #Es el contorno inferior de un pilar                        
                        elif (x,y) in self._cont_inf:
                            self._matrix[y][x] = 0.25 * (2 * self._matrix[y + 1][x] + self._matrix[y][x - 1] + self._matrix[y][x + 1])

                        else:
                            #Pilar
                            if np.isnan(self._matrix[y][x]):
                                continue

                            #general
                            self._matrix[y][x] = 0.25 * (self._matrix[y - 1][x] + self._matrix[y + 1][x] + self._matrix[y][x - 1] + self._matrix[y][x + 1])



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


    def addPilar(self, x, y):

        """        
        Añade un pilar al Rio
        
        Las grillas adyacentes de un pilar las denominamos contorno
        el contorno de un pilar no puede coincidir (en ninguna grilla) con el contorno de otro pilar
        Tampoco puede haber contornos que coincidinan con el "borde del rio"

        :param x: (int) coordenada x centro pilar
        :param y: (int) coordenada y centro pilar
        :return: (bool) - True si pilar puede ser añadido
                        - False si no

        """
        med_pilar = int(self._adh/2)
        x1 = x - med_pilar
        x2 = x + med_pilar
        y1 = y - med_pilar
        y2 = y + med_pilar

        if x1<2 or x2>self._w-2 or y1<2 or y2>self._h-2:
            print("[Error]: No se puede poner un pilar tan cerca del borde!")
            return False


        for pilar in self._pilares:
            if (abs(pilar[0] - x) < 2*med_pilar+2 and abs(pilar[1] - y) < 2*med_pilar+2 ):
                if (abs(pilar[1] - y)==2*med_pilar and abs(pilar[0] - x) == 2*med_pilar+1) or (abs(pilar[1] - y)==2*med_pilar+1 and abs(pilar[0] - x) == 2*med_pilar):
                    continue
                print("[Error]: No se puede poner un pilar tan cerca de otro!")
                return False

        _cont_izq = []
        _cont_der = []
        _cont_inf = []
        _cont_sup = []

        for _y in range(y1,y2):
            for _x in range(x1,x2):
                self._matrix[_y][_x] = None
            _cont_izq.append((x1-1, _y))
            _cont_der.append((x2, _y))

        for n in range(x1,x2,1):            
            _cont_sup.append((n, y1-1))
            _cont_inf.append((n, y2))
        
        self._cont_der+=_cont_der
        self._cont_izq+=_cont_izq
        self._cont_inf+=_cont_inf
        self._cont_sup+=_cont_sup
        self._pilares.append((x,y))
        
        self._contornos = self._cont_der + self._cont_izq + self._cont_sup + self._cont_inf

        return True

    def addPilarMetros(self,x,y):

        """        
        Añade un pilar al Rio
        
        :param x: (int)/(float) posición x del centro pilar
        :param y: (int)/(float) posicion y centro pilar
        :return: (bool) - True si pilar puede ser añadido
                        - False si no

        este metodo llama a addPilar

        """
        _x = int( x / self._dh)        #convertir metros a coordenadas
        _y = int( y / self._dh)
        print _x
        print _y
        return self.addPilar( _x , _y)


    def show_map(self):

        """
        Grafica el mapa del rio (pilares y contornos)
        :return: None
        """

        for point in self._contornos:
            self._rio[point[1]][point[0]] = 1

        fig = plt.figure()
        ax = fig.add_subplot(111)
        # # Se agrega grafico al plot
        

        cax = plt.imshow(self._rio, cmap='Greys',  interpolation='nearest')

        #grillas diferenciales        
        for k in range(1, self._w):
            plt.axvline(x=k-0.5, color=(0,0,0,0.5), linestyle='--', lw=0.5)

        for m in range(1, self._h):
            plt.axhline(y=m-0.5, color=(0,0,0,0.5), linestyle='--', lw=0.5)

        #coordenadas en metros
        for i in range(1, int(self._largo)+1):
            plt.axvline(x=i/self._dh-0.5, color='k', linestyle='--', lw=1.0)
        
        for j in range(1, int(self._ancho)+1):
            plt.axhline(y=j/self._dh-0.5, color='k', linestyle='--', lw=1.0)

        #Bordes del rio
        plt.axvline(x=self._w-0.5, color='r', linestyle='--', lw=1.0)
        plt.axvline(x=-0.5, color='r', linestyle='--', lw=1.0)

        plt.axhline(y=self._h-0.5, color='r', linestyle='--', lw=1.0)
        plt.axhline(y=0-0.5, color='r', linestyle='--', lw=1.0)
        
        # fig.colorbar(cax)
        plt.show()    

    def print_rio(self):
        """
        imprime la matriz que representa el mapa del rio
        :return: None
        """
        for point in self._contornos:
            self._rio[point[1]][point[0]] = 1
        
        print(self._rio)

    def get_presion(self):
        """
        Retorna el promedio de presión en la boca del rio
        :return: (float)
        
        """

        last_colum = self._matrix[:,self._w-1]
        return np.mean(last_colum)



def main():
    # Instancia rio

    print(" -- Simulador de Presiones en Rio -- ")
    print("Dimensiones del Rio: ")
    ancho = input("Ancho en metros: ")
    largo = input("Largo en metros: ")
    
    grilla  = input("Tamaño de la grilla en metros: ")
    
    r = Rio(ancho, largo, grilla)

    pilares  = input("Numeros de Pilares?: ")

    n = 1
    while n<=pilares:
        print("-- Pilar {0} --".format(n))
        x = input("posición x: ")
        y = input("posición y: ")
        a = r.addPilar(x,y)
        if a:
            print("Ok!")
            n+=1
        else:
            print("Pilar inválido :(! ")
            continue
    
    r.cb(1)
    r.show_mapa()
    r.start()
    r.imprime()
    r.plot()

def medir_presiones(rio, pos_x):

    """
    Recibe un rio y una coordenada en X

    :param rio:
    :param pos_x:
    :return: None
    """

    presion_rio_abajo = []
    pos=[]
    rio.reset()
    
    for pos_y in range(0, rio._h):

        a = rio.addPilar(pos_x, pos_y)
        if not(a):
            continue
        
        rio.old_cb(1)
        rio.start()
        presion_rio_abajo.append(rio.get_presion())
        pos.append(pos_y*rio._dh)
        rio.reset()
    
    graph = plt.plot(pos, presion_rio_abajo, color='red', marker='o', linestyle='none', linewidth=2, markersize=12, label = "presion desembocadura rio ")
    vert_line = plt.axvline(x=rio._ancho/2.0, label = "centro del rio")
    plt.xlabel('Distancia de Borde Superior a Centro de Pilar[ m ]')
    plt.ylabel('Presion Promedio en Boca del Rio [ Pascal(?) ]')
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=1, borderaxespad=0)    
    print(presion_rio_abajo)
    plt.show()

def _test_medir_presion():
    r = Rio(3.5, 7, 0.25) # rio de 3.5 metros de ancho, 7 de largo y una grilla de 0.25 metros de lado
    pos_x = int(r._w/2) # ubicamos el pilar a mitad de rio en eje x para luego iterarlo en eje y
    medir_presiones(r, pos_x)



if __name__ == '__main__':
    main() 