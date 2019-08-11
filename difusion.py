#!/usr/bin/python
from matplotlib import pyplot as plt
import numpy as np
import random 
from math import sqrt

def grafica(x,y):
	plt.plot(x,y,color='blue')
	plt.xlabel('t')
	plt.ylabel('Xt')
	plt.title('Selection balancing')
	plt.show()
        
def MB(n,T):
	Z = []
	particion = np.linspace(0,T,n)
	for i in range(n):
		Z.append((float(np.random.normal(0,1,1)))*(sqrt(T/n)))
	S = np.cumsum(Z)
	return particion,S

def difusion(a,k,x0,T):
    M = MB(5000,T)
    X = [x0]
    t = list(M[0])
    W = list(M[1])
    for i in range(len(t)-1):
        if X[i] >= 1:
            return t[0:len(X)],X
        elif X[i]<=0:
            return t[0:len(X)],X
        else:
            Xt = X[i]
            w = Xt -a*Xt*(1-Xt)*(t[i+1]-t[i]) + k*Xt*(1-Xt)*(1-k*Xt)+ sqrt(Xt*(1-Xt)*(1-k*Xt))*(W[i+1]-W[i])
            X.append(w)
    return t[0:len(X)],X

Proceso = difusion(0.05,0.001,0.5,2)
x = Proceso[0]
y = Proceso[1]
grafica(x,y)
