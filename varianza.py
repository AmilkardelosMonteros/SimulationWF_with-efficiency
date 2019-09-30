#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

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
            probas.append(vector[Inc[j]+i][2])
            err.append(0.5*np.sqrt((vector[Inc[j]+i][3])/5000))
        Equis.append(equis)
        Probas.append(probas)
        Err.append(err)
    Kapa = np.linspace(0,0.9,20) #Ojo aqui, depende del modelo eficiencia es(0,0.9) y longevidad es (0,1)
    K = [0,4,8,12,17,19]
    for indice in K:
        plt.errorbar(Equis[indice],Probas[indice],label = 'k = '+ str(Kapa[indice]),yerr = Err[indice])
    mpl.rc('xtick', labelsize=17) 
    mpl.rc('ytick', labelsize=17)
    plt.legend(loc='upper left')
    plt.xlabel('$s $', fontsize = 40)
    plt.ylabel('', fontsize = 40)
    plt.show()


errores(x)
