
import matplotlib.pyplot as plt
import numpy as np

X = np.loadtxt('Eficiencia_u1_0.01_u2_0.001.txt')


def grafica(a):
    x = []
    y = []
    for i in range(len(a)):
        tem = a[i]
        x.append(tem[0])
        y.append(tem[1])
    plt.xlim(-0.07,0.07)
    plt.ylim(-0.2,1.2)
    plt.plot(x,y,'o',alpha = 0.05)
    plt.show()

grafica(X)
def lado(x,y):
    if y > 0.97:
        return 1
    elif x > 0.049 and  y < 0.97:
        return 2
    elif x < -0.049 and  y < 0.97:
        return 3
    else:
        return 4
    
def aux2(a,graf):
    arriba = []
    derecha = []
    izquierda = []
    abajo = []
    for i in range(len(a)):
        s = a[i]
        pos = lado(s[0],s[1])
        if pos == 1:
            arriba.append(s[0])
        elif pos == 2:
            derecha.append(s[1])
        elif pos ==3:
            izquierda.append(s[1])
        elif pos == 4:
            abajo.append(s[0])
    if graf == False:
        return [arriba,derecha,izquierda,abajo]
    else:
        print(len(arriba))
        plt.subplot(2,2,1)
        plt.hist(arriba,label = 'arriba '+str(len(arriba)))
        plt.legend()
        plt.subplot(2,2,2)
        plt.hist(derecha,label = 'derecha ' + str(len(derecha)))
        plt.legend()
        plt.subplot(2,2,3)
        plt.hist(izquierda,label = 'izquiera ' +str(len(izquierda)))
        plt.legend()
        plt.subplot(2,2,4)
        plt.hist(abajo,label = 'abajo ' + str(len(abajo)))
        plt.legend()
        plt.show()


aux2(X,True)
