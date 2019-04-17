#Gazque Espinosa de lo Monteros Edgar Amilkar
from matplotlib import pyplot as plt
import numpy as np
import random 
import math
import matplotlib.pyplot as plt
x1 = 0.5
N = 10**2

def grafica(x,y):
	plt.plot(x,y,color='blue')
	plt.xlabel('t')
	plt.ylabel('Xt')
	plt.title('Wright Fisher con Eficiencia k')
	plt.show()
        
def graficaC(x,y):
    plt.plot(x,y,color = 'navy')
    plt.xlabel('t')
    plt.ylabel('Wt')
    plt.xlim(-1, 1)
    plt.ylim(-1,1)
    plt.title('Caminata aleatoria en KxS')
    plt.show()
    
def ganador(k1,s1,k0,s0):
    x = [x1]
    while x[-1] != 0 and x[-1] != 1:
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
    return float(x[-1])



def puntos(n,mu1,mu2):
    perdedores = []
    ganadores = []
    for i in range(n):
        muestra = [float(mu1*np.random.uniform(0,1,1)),float(mu2*np.random.uniform(-1,1,1))]#eficiencia,seleccion
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
    for i in range(len(per)):
        x1.append(per[i][0])
        y1.append(per[i][1])
    for j in range(len(gan)):
        x2.append(gan[j][0])
        y2.append(gan[j][1])
    plt.plot(y1,x1,'ro')
    plt.plot(y2,x2,'bo')
    plt.show()
#p = puntos(100,0.4,0.05)
#grafica_puntos(p)



def distribucion(v,mu1,mu2):
        return v[-1][0]+ mu1*np.random.uniform(-1,1,1), v[-1][1] + mu2*np.random.uniform(-1,1,1)
    
def Mutacion1(n,mu1,mu2):
    trayectoria =  [[0,0]]
    for i in range(n):
        print(trayectoria[-1])
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
                print(trayectoria[-1])
                volado = np.random.binomial(1,0.5,1)
                if volado == 1: #Se muta solo el parametro de la eficiencia
                        retador = distribucion(trayectoria,mu1,0)
                        if abs(trayectoria[-1][0]) >= 1 or abs(trayectoria[-1][1]) >= 1:  
                                return trayectoria
                        elif abs(retador[0]) >=1 or abs(retador[1]) >= 1:
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
                        
                                
                        





        

def dibuja_mutacion1(trayectoria):
        x = []
        y = []
        for i in range(len(trayectoria)):
                v = trayectoria[i]
                x.append(v[0])
                y.append(v[1])
        graficaC(x,y)

    
C = Mutacion2(10,1,0.05)
#print(len(C))
dibuja_mutacion1(C)
