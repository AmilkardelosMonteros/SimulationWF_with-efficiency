#!/usr/bin/python
import sys
import os
import numpy as np
import time
N = int(sys.argv[1])
s = float(sys.argv[2])/float(N)
rep = int(sys.argv[3])
k = float(sys.argv[4])
x1 = 0.5
print('Corriendo Simulacion los siguientes parametros:')
print(N,s,rep,k)
def ganador(N,s,k):
    s1 = s
    k0 = k
    x = x1
    while x > 0 and x < 1:
        C = 0
	D = 0
	M = 0
	while C < N:
            f = x
            A = np.random.binomial(1,((1+s1)*f)/((1+s1)*f+(1-f)))
            D += A
            C += A + (1-A)*(1-k0)
            M += 1
        x=float(D)/M
    return x

def proba(N,s,rep,k):
    nombre = 'EfectodeN'+'_N_' + str(N)+ '_rep_'+ str(rep) + '_s_' + str(s) + '_k_' + str(k) +'.txt'
    archivo = open(nombre,'a')
    if os.stat(nombre).st_size == 0:
        np.savetxt(nombre,[0])
    iter = np.loadtxt(nombre)
    archivo.close()
    for i in range(rep):
        archivo = open(nombre,'a')
        iter = np.append(iter,ganador(N,s,k))
        np.savetxt(nombre,iter[1:])
        archivo.close()



proba(N,s,rep,k)
