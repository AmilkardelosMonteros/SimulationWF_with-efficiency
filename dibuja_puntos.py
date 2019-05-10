#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

archivo = open('un_archivo.txt','r')
vector =  archivo.read()
print(vector)

def dibuja_puntos(arreglo):
    x = []
    y = []
    info = []
    for i in range(len(arreglo)):
        v = arreglo[i]
        x.append(v[0])
        y.append(v[1])
        info.append(v[2])
    fig, ax = plt.subplots()
    plt.scatter(x,y, s=8**2, c = info, alpha = 0.7)
    plt.colorbar()
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.yaxis.tick_left()
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')
    plt.xlabel('s', fontsize = 15)
    plt.ylabel(r"$\kappa$", fontsize = 15)
    plt.show()
archivo.close()
