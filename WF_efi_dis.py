#Gazque Espinosa de lo Monteros Edgar Amilkar
from matplotlib import pyplot as plt
import numpy as np
import random 
import math
import matplotlib.pyplot as plt
def grafica(x,y):
	plt.plot(x,y,color='blue')
	plt.xlabel('t')
	plt.ylabel('Xt')
	plt.title('Wright Fisher con Eficiencia k')
	plt.show()
#0 son los eficientes 
#1 los ineficientes
vector_inicial = []

kapa = 0.4
N = 20**2#Cantidad de Recursos
s = 0.008#parametro de la seleccion

size0 = 10
size1 = 5
for i in range(size0):
	vector_inicial.append(0)
for i in range(size1):
	vector_inicial.append(1)

def Bernoulli(p):
	b = random.random()
	if b < p:
		return 0
	else:
                return 1

def Y_n(vector):
	suma = 0
	for i in range(len(vector)):
		if vector[i] == 0:
			suma = suma + 1
	return (suma)/len(vector)

def suerte1(vector):
	return Bernoulli(Y_n(vector))

def suerte2(vector):
	x = Y_n(vector)
	proba = (x)/(x + (1-x)*(1-s)) #assuming that the efficient ones have an advantage s
	return Bernoulli(proba)

def Consumo(vector):
	suma1 = 0
	suma0 = 0
	for i in range(len(vector)):
		if vector[i] == 0:
			suma0 = suma0 + 1
		else:
			suma1 = suma1 + 1

	return suma1 + (1-kapa)*suma0

def Proceso1(n):
	proceso = [vector_inicial]
	for i in range(n):
		vec_aux = [suerte1(proceso[i])]
		while Consumo(vec_aux) < N:
			vec_aux.append(suerte1(proceso[i]))
		proceso.append(vec_aux)
	return(proceso)


def Proceso2(n):
	proceso = [vector_inicial]
	for i in range(n):
		vec_aux = [suerte2(proceso[i])]
		while Consumo(vec_aux) < N:
			vec_aux.append(suerte2(proceso[i]))
		proceso.append(vec_aux)
	return(proceso)

def Frecuencia(Proceso):
	vector = []
	for i in range(len(Proceso)):
		vector.append(Y_n(Proceso[i]))
	return vector


x = 0.5 #frecuencia de los eficientes
def PROCESO(n):
        proceso = [x]
        for i in range(n):
                vector_aux = []
                while Consumo(vector_aux) < N:
                        vector_aux.append(Bernoulli(proceso[i]))
                proceso.append(Y_n(vector_aux))
                if proceso[i] == 1 or proceso[i]==0:
                        break
        return proceso
#X_n = Proceso1(300)
#X_n = Proceso2(300)
#Y = Frecuencia(X_n)
#x = np.linspace(0,len(X_n),len(X_n))
#grafica(x,Y)

y = PROCESO(500)
x= np.linspace(0,len(y),len(y))
grafica(x,y)

