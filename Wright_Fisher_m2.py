#!/usr/bin/python
import sys
from multiprocessing import Pool
import numpy as np
import time
from matplotlib import pyplot as plt
param = sys.argv[1]
Param = int(param)
x1 = 0.5
N = 100

def ganador(parametros):
    k1 = parametros[0]
    s1 = parametros[1]
    k0 = parametros[2]
    s0 = parametros[3]
    x = x1
    while x > 0 and x < 1:
        C = 0
	D = 0
	M = 0
	cierto = True
        while C < N and cierto:
            f = x
            A = np.random.RandomState().binomial(1,((1+s1)*f)/((1+s1)*f+(1+s0)*(1-f)))
            if C + A*(1-k1) + (1-A)*(1-k0) < N:
                D += A
                C += A*(1-k1) + (1-A)*(1-k0)
                M += 1
            else:
                cierto = False
        x = float(D)/M
    return x

def proba(k,s,repeticiones):
    p = Pool()
    parametros = [k,s,0,0]
    iter = []
    for i in range(repeticiones):
        iter.append(parametros)
    informacion = p.map(ganador,iter)
    todo = [s,k,np.mean(informacion),np.var(informacion)]
    return todo
def puntos(n,m,repeticiones,numero,nombre):
    S = np.linspace(-0.025,0.025,n)
    s = S[numero]
    K = np.linspace(0,0.9,m)
    archivo = open(nombre,'a')
    for k in K:
        WF = proba(k,s,repeticiones)
        archivo.write(str(WF) + ',')
    archivo.close()

def funcion(numero):
    nombre = 'm2_' + str(int(numero)) + '.txt'
    puntos(20,20,5000,numero,nombre)

funcion(Param)