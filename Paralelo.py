#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool
x1 = 0.5
N = 1000

def ganador(k1,s1,k0,s0):
    x = x1
    while x > 0 and x < 1:
        C = 0
        D = 0
        M = 0
        while C < N:
            f = x
            A = np.random.binomial(1,((1+s1)*f)/((1+s1)*f+(1+s0)*(1-f)))
            D += A
            C += A*(1-k1) + (1-A)*(1-k0)
            M += 1
        x=float(D)/M
    return x

def puntos(n,m,repeticiones,numero,nombre):
    S = np.linspace(-0.005,0.005,n)
    s = S[numero]
    K = np.linspace(0.2,0.8,m)
    for k in K:
        WF = []
        for i in range(int(repeticiones)):
            #g = ganador(k,s,0,0)
            g = np.random.binomial(1,0.5)
            WF.append(g)
        archivo = open(nombre,'a')
        archivo.write(str([s,k,np.mean(WF),np.var(WF)]) + ',')
    archivo.close()
    
def funcion(numero):
    nombre = 'un_archivo' + str(int(numero)) + '.txt'
    archivo = open(nombre,'w')
    puntos(20,20,20.0,numero,nombre)

if __name__ == '__main__':
    p = Pool()
    p.map(funcion,np.linspace(7,19,13))
