#Gazque Espinosa de lo Monteros Edgar Amilkar
from matplotlib import pyplot as plt
import numpy as np
import random 
import math
import matplotlib.pyplot as plt
x1 = 0.5
N = 100
 
def ganador(k1,s1,k0,s0):
    x = [x1]
    while x[-1] > 0 and x[-1] < 1:
        C = 0
        D = 0 
        M = 0
        while C <= N:
            f = x[-1]
            A = np.random.binomial(1,((1+s1)*f)/((1+s1)*f+(1+s0)*(1-f)))
            D += A
            C += A*(1-k1) + (1-A)*(1-k0)
            M += 1
        x[0]=float(D)/M
    return int(float(x[-1]))


def distribucion(v,mu1,mu2):
        return v[-1][0]+ mu1*np.random.uniform(-1,1,1), v[-1][1] + mu2*np.random.uniform(0,1,1)#s,k

def Mutacion1(n,mu1,mu2):
    trayectoria =  [[0,0]] #s,k
    for i in range(n):
        print(i)
        retador = distribucion(trayectoria,mu1,mu2)
        if abs(trayectoria[-1][0]) >= 1 or trayectoria[-1][1] > 1 or trayectoria[-1][1] < 0:  
            return trayectoria
        elif abs(retador[0]) >=1 or retador[1] > 1 or retador[1] < 0:
                return trayectoria
        elif ganador(trayectoria[-1][1],trayectoria[-1][0],retador[1],retador[0]) == 1:#k1,s1,k2,s2
            trayectoria.append([trayectoria[-1][0],trayectoria[-1][1]])
        else:
            trayectoria.append([retador[0],retador[1]])
    return trayectoria

def dibujo(trayectoria):
    x = []
    y = []
    for i in range(len(trayectoria)):
        v = trayectoria[i]
        x.append(v[0])
        y.append(v[1])
    plt.plot(x,y,color='blue')
    plt.xlabel('seleccion')
    plt.ylabel('mutacion')
    plt.xlim(-1,1)
    plt.ylim(0,1)
    plt.show()

#C  = Mutacion1(100,0.05,0.04)#pasos,seleccion,mutacion
#dibujo(C)

def caminatas(m,n): #m es el numero de caminatas y n es el numero de pasos de cada 1
    X = []
    Y = []
    for i in range(m):
        print('#################')
        print(i)
        print('#################')
        C = Mutacion1(n,0.06,0.03)
        x = []
        y = []
        for i in range(len(C)):
            v = C[i]
            x.append(v[0])
            y.append(v[1])
        X.append(x)
        Y.append(y)
    #plt.plot(X[-1],Y[-1],color = 'red')
    plt.plot(X[0],Y[0],X[1],Y[1],X[2],Y[2],X[3],Y[3],X[4],Y[4])#,X[5],Y[5],X[6],Y[6],X[7],Y[7],X[8],Y[8],X[9],Y[9],X[10],Y[10],X[11],Y[11],X[12],Y[12],X[13],Y[13],X[14],Y[14],X[15])#,Y[15],X[16],Y[16],X[17],Y[17],X[18],Y[18],X[19],Y[19],X[20],Y[20],X[21],Y[21],X[22],Y[22],X[23],Y[23],X[24],Y[24],X[25],Y[25])
    plt.xlim(-1, 1)
    plt.ylim(0,1)
    plt.show()
           
caminatas(5,300)
