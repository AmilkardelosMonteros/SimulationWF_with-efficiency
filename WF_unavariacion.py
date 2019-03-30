#Gazque Espinosa de lo Monteros Edgar Amilkar
from matplotlib import pyplot as plt
import numpy as np
import random 
import math
import matplotlib.pyplot as plt
parametros = [0.2,0.3,0,0]#k1,k2,s1,s2
x1 = 0.5
N = 10**2
def grafica(x,y):
	plt.plot(x,y,color='blue')
	plt.xlabel('t')
	plt.ylabel('Xt')
	plt.title('Wright Fisher_'+'k1='+str(parametros[0])+',k2='+str(parametros[1])+',s1='+str(parametros[2])+',s2='+str(parametros[3]))
	plt.show()
	
def Bernoulli(x):
        u = random.random()
        if u <= x:
                return 1
        else:
                return 0

def consumo(k1,k2,vector):
        suma = 0
        for i in range(len(vector)):
                if vector[i]==1:
                        suma = suma + (1-k1)
                else:
                        suma = suma + (1-k2)
        return suma

def frecuencia(vector):
	suma = 0
	for i in range(len(vector)):
		if vector[i] == 1:
			suma = suma + 1
	return (suma)/len(vector)

def WF(k1,k2,s1,s2):
        proceso = [x1]
        i = 0
        while proceso[i]!=0 or proceso[i] !=1:
                vector_aux = []
                while consumo(k1,k2,vector_aux) < N:
                        x = proceso[i]
                        p = ((1+s1)*x)/((1-s1)*x+(1+s2)*(1-x))
                        vector_aux.append(Bernoulli(p))
                proceso.append(frecuencia(vector_aux))
                i=i+1
                if proceso[i] == 1 or proceso[i]==0:
                        break
        return proceso

def ganador(k1,k2,s1,s2):
        Proceso =  WF(k1,k2,s1,s2)
        return Proceso[-1]
p = parametros       
y = WF(p[0],p[1],p[2],p[3])
x= np.linspace(0,len(y),len(y))
grafica(x,y)
