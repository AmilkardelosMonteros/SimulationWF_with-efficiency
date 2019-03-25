#Gazque Espinosa de los Monteros Edgar Amilkar
from matplotlib import pyplot as plt
import numpy as np
import random 
import math
from matplotlib.animation import FuncAnimation
        
def grafica(x,y):
	plt.plot(x,y,color='blue')
	plt.xlabel('t')
	plt.ylabel('Xt')
	plt.title('Wright Fisher with-efficiency k')
	plt.show()

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
	for i in range(len(t)-1):
           
            if X[i] >= 1:
                w = 1
                X.append(w)
            elif X[i]<=0:
                w = 0
                X.append(w)

            else:
                w = X[i]-alfa*X[i]*(t[i+1]-t[i]) + (math.sqrt(X[i]*(1-X[i])*(1-kapa*X[i])))*(W[i+1]-W[i])
                X.append(w)
	return t,X

Proceso = WF_efic(0,0.25,0.5,2)
x = Proceso[0]
y = Proceso[1]
grafica(x,y)
