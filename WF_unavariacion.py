
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
        
def graficaC(x,y,pasos,rep):
    plt.plot(x,y,color = 'navy')
    plt.xlabel('t')
    plt.ylabel('Wt')
    plt.xlim(-1, 1)
    plt.ylim(-1,1)
    plt.title('Caminata aleatoria_de'+str(pasos)+ '_en KxS con_'+ str(rep)+'_repeticiones')
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
        
#C = Mutacion1(100,0.01,0.03)
#dibuja_mutacion1(C)
def MB(n,T):
	Z = []
	particion = np.linspace(0,T,n)
	for i in range(n):
		Z.append((float(np.random.normal(0,1,1)))*(math.sqrt(T/n)))
	S = np.cumsum(Z)
	return particion,S
    
def WF_efic(alfa,kapa,frecuencia,T):
    M = MB(4000,T)
    X = [frecuencia]
    t = list(M[0])
    W = list(M[1])
    i = 0
    paro = True
    while paro and i < len(t)-1:
        if X[-1] >= 1 or X[-1]<= 0:
            paro = False
            return X
        w = X[i]-alfa*X[i]*(t[i+1]-t[i]) + (math.sqrt(X[i]*(1-X[i])*(1-kapa*X[i])))*(W[i+1]-W[i])
        i = i + 1
        X.append(w)
       
    return X

Proceso = WF_efic(0,0.25,0.5,2)
print(Proceso)
