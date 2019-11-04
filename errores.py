#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import scipy as scipy
import scipy.linalg
from itertools import *
from random import *
import scipy.special as special
import scipy.integrate as integrate

def probafixM1(a, k, y):
    if 2*a < k:
        S = 1 - (1 - k)**(1 - 2*a/k)
        p = (1/S)* (1-(1 - k*(1-y))**(1 - 2*a/k))
    elif 2*a == k :
        S = np.log(1.0/(1.0-k))
        p = (1/S)*np.log(1.0/(1.0-k*(1-y)))
    else :
        S = (1 - k)**(1 - 2*a/k)  - 1
        p = (1/S)* ((1 - k*(1-y))**(1 - 2*a/k)-1)
    return 1-p



##### ESTO ES EL MODELO M2 para k=a/b, k en (0, 1/2) (i) del Thm 3
def scaleintM2(a,k,y): #esto solo es un intermediario para calcular probafix
    result = integrate.quad(lambda x: np.exp(-2*k*x)*(1-k*x)**(-2*a/k), y, 1)
    return result[0]


def probaM2(a,b,y):
    p = scaleintM2(a,b,1-y)/scaleintM2(a,b,0)
    return p

Kapa = np.linspace(0,0.9,20)
S = np.linspace(-0.025,0.025,1000)
#K = [3,7,10,13,16]
K = [3,7,9]
colores = ['b','g','r','c','m']
for i in range(len(K)):
    P = []
    print(Kapa[K[i]])
    for s in S:
        #P.append(probafixM1(-s*100,Kapa[K[i]],0.5))
        #P.append(probaM2(s*100,Kapa[K[i]],0.5))
    plt.plot(S,P,colores[i])



def errores(vector):
    Equis = []
    Probas = []
    Err = []
    Inc = range(0,399,20)
    for i in range(20):
        equis = []
        probas = []
        err =  []
        for j in range(20):
            equis.append(vector[Inc[j]+i][0])
            probas.append(1-(vector[Inc[j]+i][2]))
            err.append(0.5*np.sqrt((vector[Inc[j]+i][3])/5000))
        Equis.append(equis)
        Probas.append(probas)
        Err.append(err)
     #Kapa = np.linspace(0,0.9,20) #Ojo aqui, depende del modelo eficiencia es(0,0.9) y longevidad es (0,1)
     #K = [3,7,10,13,16]
    for i in range(len(K)):
        plt.errorbar(Equis[K[i]],Probas[K[i]],label = 'k = '+ str(Kapa[K[i]]),yerr = Err[K[i]],fmt='.',color = colores[i])
        plt.plot(0,0.5,'x')
    mpl.rc('xtick', labelsize=17) 
    mpl.rc('ytick', labelsize=17)
    plt.legend(loc='upper letf')
    plt.xlabel('$s $', fontsize = 30)
    plt.ylabel('Probability of fixation', fontsize = 20)
    plt.show()


errores(x)


