#Gazque Espinosa de lo Monteros Edgar Amilkar
from matplotlib import pyplot as plt
import numpy as np
import random 
import math
import matplotlib.pyplot as plt
#parametros = [0.2,0.3,0,0]#k1,k2,s1,s2
x1 = 0.5
N = 10**2
def grafica(x,y):
	plt.plot(x,y,color='blue')
	plt.xlabel('t')
	plt.ylabel('Xt')
	plt.title('Wright Fisher_'+'k1='+str(parametros[0])+',k2='+str(parametros[1])+',s1='+str(parametros[2])+',s2='+str(parametros[3]))
	plt.show()
	
def graficaC(x,y):
    plt.plot(x,y,color='blue')
    plt.xlabel('t')
    plt.ylabel('Zt')
    plt.title('Caminata aleatoria en KxS')
    plt.show()

def consumo(k1,k2,vector):
        suma = 0
        for i in range(len(vector)):
                if vector[i]==1:
                        suma = suma + (1-k1)
                else:
                        suma = suma + (1-k2)
        return suma


def frecuencia(vector):
        return sum(vector)/len(vector)

def ganador(k1,k2,s1,s2):
        frec = x1
        while frec!=0 or frec !=1:
                vector_aux = []
                while consumo(k1,k2,vector_aux) < N:
                        x = frec
                        p = ((1+s1)*x)/((1+s1)*x+(1+s2)*(1-x))
                        vector_aux.append(np.random.binomial(1,p,1))
                frec = frecuencia(vector_aux)
                if frec == 1 or frec==0:
                        break
        return frec

def distribucion2():
        v = True
        while v:
                x = 2*random.random()-1
                y = 2*random.random()-1
                if x**2 + y**2 <= 1:
                        v = False
        return x,y

def Caminata(n):
        trayectoria = [[0,0]]
        for i in range(n):
                retador = distribucion2(1)
                vence = ganador(trayectoria[-1][0],trayectoria[-1][0],retador[0],retador[1])
                if vence == 0:
                        trayectoria.append([retador[0],retador[1]])
        return trayectoria 
                
                
def dibuja_caminata(trayectoria):
        x = []
        y = []
        for i in range(len(trayectoria)):
                v = trayectoria[i]
                x.append(v[0])
                y.append(v[1])
        graficaC(x,y)

C=Caminata(10)        
#print(C)
dibuja_caminata(C)



