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

def Frecuencia(Proceso):
	vector = []
	for i in range(len(Proceso)):
		vector.append(Y_n(Proceso[i]))
	return vector

X_n = Proceso1(300)
Y = Frecuencia(X_n)
x = np.linspace(0,len(X_n),len(X_n))
grafica(x,Y)
