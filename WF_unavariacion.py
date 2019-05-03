#Gazque Espinosa de lo Monteros Edgar Amilkar
from matplotlib import pyplot as plt
import numpy as np
import random 
import math
import matplotlib.pyplot as plt
x1 = 0.5
N = 100

def grafica(x,y):
    plt.plot(x,y,color='blue')
    plt.xlabel('t')
    plt.ylabel('Xt')
    plt.title('Wright Fisher con Eficiencia k')
    plt.show()
        
def graficaC(x,y,pasos,rep):
    y1 = np.linspace(-1,1,10)
    x1 = np.linspace(0,0,10)
    plt.plot(x1,y1,'r.')
    plt.plot(x,y,color = 'navy')
    plt.xlabel('t')
    plt.ylabel('Wt')
    plt.xlim(-1, 1)
    plt.ylim(-1,1)
    plt.title('Caminata aleatoria_de'+str(pasos)+ '_en KxS con_'+ str(rep)+'_repeticiones')
    plt.show()
    
def ganador(k1,s1,k0,s0):
    x = [x1]
    while x[-1] > 0 and x[-1] < 1:
        C = 0
        D = 0 
        M = 0
        while C <= N:
            f = x[-1]
            #print(f)
            A = np.random.binomial(1,((1+s1)*f)/((1+s1)*f+(1+s0)*(1-f)))
            D += A
            C += A*(1-k1) + (1-A)*(1-k0)
            M += 1
        x[0]=float(D)/M
    return int(float(x[-1]))

def puntos(n,mu1,mu2):
    perdedores = []
    ganadores = []
    for i in range(n):
        muestra = [float(mu1*np.random.uniform(-1,1,1)),float(mu2*np.random.uniform(-1,1,1))]#eficiencia,seleccion
        if ganador(0,0,muestra[0],muestra[1]) == 0:
            ganadores.append(muestra)
        else:
            perdedores.append(muestra)
    return [perdedores,ganadores]
    
def grafica_puntos(puntos):
    per = puntos[0]
    gan = puntos[1]
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    p = len(per)
    g = len(gan)
    for i in range(p):
        x1.append(per[i][0])
        y1.append(per[i][1])
    for j in range(g):
        x2.append(gan[j][0])
        y2.append(gan[j][1]) 
    total = p + g
    plt.plot(x1,y1,'ro')
    plt.plot(x2,y2,'bo')
    plt.title('Ganadores(azules)=' + str(g)+',Numero total de puntos =_' + str(total))
    plt.show()
#p = puntos(100,0.4,0.01)
#grafica_puntos(p)



def distribucion(v,mu1,mu2):
        return v[-1][0]+ mu1*np.random.uniform(-1,1,1), v[-1][1] + mu2*np.random.uniform(-1,1,1)
    
def Mutacion1(n,mu1,mu2):
    trayectoria =  [[0,0]]
    for i in range(n):
        print(i)
        retador = distribucion(trayectoria,mu1,mu2) #[float(mu1*np.random.uniform(0,1,1)),float(mu2*np.random.uniform(-1,1,1))]
        if abs(trayectoria[-1][0]) >= 1 or abs(trayectoria[-1][1]) >= 1:  
            return trayectoria
        elif abs(retador[0]) >=1 or abs(retador[1]) >= 1:
                return trayectoria
        elif ganador(trayectoria[-1][0],trayectoria[-1][1],retador[0],retador[1]) == 1:#k1,s1,k2,s2
            trayectoria.append([trayectoria[-1][0],trayectoria[-1][1]])
        else:
            trayectoria.append([retador[0],retador[1]])
    return trayectoria
                    
            
def Mutacion2(n,mu1,mu2):
        trayectoria =  [[0,0]]
        for i in range(n):
                volado = np.random.binomial(1,0.5,1)
                if volado == 1: #Se muta solo el parametro de la eficiencia
                        retador = distribucion(trayectoria,mu1,0)
                        if abs(trayectoria[-1][0]) >= 1 or abs(trayectoria[-1][1]) >= 1:  
                                return trayectoria
                        elif abs(retador[0]) >=1 or abs(retador[1]) >= 1:
                                trayectoria.append([retador[0],retador[1]])
                                return trayectoria
                        elif ganador(trayectoria[-1][0],trayectoria[-1][1],retador[0],retador[1]) == 1:#k1,s1,k2,s2
                                trayectoria.append([trayectoria[-1][0],trayectoria[-1][1]])
                        else:
                                trayectoria.append([retador[0],retador[1]])
                                

                else:
                        retador = distribucion(trayectoria,0,mu2)
                        if abs(trayectoria[-1][0]) >= 1 or abs(trayectoria[-1][1]) >= 1:  
                                return trayectoria
                        elif abs(retador[0]) >=1 or abs(retador[1]) >= 1:
                                return trayectoria
                        elif ganador(trayectoria[-1][0],trayectoria[-1][1],retador[0],retador[1]) == 1:#k1,s1,k2,s2
                                trayectoria.append([trayectoria[-1][0],trayectoria[-1][1]])
                        else:
                                trayectoria.append([retador[0],retador[1]])

        return trayectoria
                        
def Mutacion3(mu1,mu2):
    trayectoria =  [[0,0]]
    i = 1
    while abs(trayectoria[-1][0]) <= 1 and abs(trayectoria[-1][1]) <= 1:
        print(i)
        retador = distribucion(trayectoria,mu1,mu2)
        if abs(retador[0]) >= 1 or abs(retador[1]) >= 1:
                return trayectoria
        elif ganador(trayectoria[-1][0],trayectoria[-1][1],retador[0],retador[1]) == 1:#k1,s1,k2,s2
            trayectoria.append([trayectoria[-1][0],trayectoria[-1][1]])
        else:
            trayectoria.append([retador[0],retador[1]])
        i = i + 1
    return trayectoria

def dibuja_mutacion1(trayectoria):
        x = []
        y = []
        repeticiones = 0
        pasos = len(trayectoria)
        for i in range(pasos):
                if i > 0:
                        if trayectoria[i][0] == trayectoria[i-1][0] and trayectoria[i][1] == trayectoria[i-1][1]:
                                repeticiones += 1
                v = trayectoria[i]
                x.append(v[0])
                y.append(v[1])
        graficaC(x,y,pasos,repeticiones)
def caminatas(m,n): #m es el numero de caminatas y n es el numero de pasos de cada 1
    X = []
    Y = []
    for i in range(m):
        print('#################')
        print(i)
        print('#################')
        C = Mutacion1(n,0.04,0.03)
        x = []
        y = []
        for i in range(len(C)):
            v = C[i]
            x.append(v[0])
            y.append(v[1])
        X.append(x)
        Y.append(y)
    #plt.plot(X[-1],Y[-1],color = 'red')
    plt.plot(X[0],Y[0],X[1],Y[1],X[2],Y[2],X[3],Y[3],X[4],Y[4],X[5],Y[5],X[6],Y[6],X[7],Y[7],X[8],Y[8],X[9],Y[9],X[10],Y[10],X[11],Y[11],X[12],Y[12],X[13],Y[13],X[14],Y[14],X[15])#,Y[15],X[16],Y[16],X[17],Y[17],X[18],Y[18],X[19],Y[19],X[20],Y[20],X[21],Y[21],X[22],Y[22],X[23],Y[23],X[24],Y[24],X[25],Y[25])
    plt.xlim(-1, 1)
    plt.ylim(-1,1)
    plt.show()
           
caminatas(16,300)

#C = Mutacion1(300,0.2,0.03)
#dibuja_mutacion1(C)
