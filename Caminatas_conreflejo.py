import numpy as np
import matplotlib.pyplot as plt
import scipy as scipy
import scipy.linalg
from itertools import *
from random import *
import scipy.special as special
import scipy.integrate as integrate
import matplotlib.pyplot as plt

u1 = 0.01 #Incremento en K (y)

u2 = 0.001 #Incremento en S (x)
frec_inicial = 0.01
#Model M1
def probafixWF(a,y): #para k = 0, (es un WF normal) a es la seleccion y y la frecuencia inicial
    p = (1-np.exp(- 2*a*y))/(1 - np.exp(-2*a))
    return p

#a es tu s, k es kappa y y es la frec inicial (1/2 para ti)
def probafixM1(a, k, y):
    if 2*a < k:
        S = 1 - (1 - k)**(1 - 2*a/k)
        p = (1/S)* (1-(1 - k*(1-y))**(1 - 2*a/k))
    elif 2*a == k:
        S = np.log(1.0/(1.0-k))
        p = (1/S)*np.log(1.0/(1.0-k*(1-y)))
    else:
        S = (1 - k)**(1 - 2*a/k)  - 1
        p = (1/S)* ((1 - k*(1-y))**(1 - 2*a/k)-1)
    return 1-p


def probabilidades(s,k):
    s_barra =  u2/(1+s)
    s_barra_neg  = -u2/(1+s)
    k_gorro = u1/(1-k)
    flag = False
    if k_gorro > 1:
        flag = True
        #import pdb; pdb.set_trace()
        
    p_gorro_mas_mas = probafixWF(s_barra,frec_inicial)
    p_gorro_menos_menos= probafixWF(s_barra_neg,frec_inicial)
        
    u_mas_mas = 1/(4*p_gorro_mas_mas)
    u_menos_mas = u_mas_mas
    u_menos_menos = 1/(4*p_gorro_menos_menos)
    u_mas_menos = u_menos_menos
   
    p_mas_mas = u_mas_mas*probafixM1((1-k)*s_barra, u1/(1-k),frec_inicial)
    p_menos_mas = u_menos_mas*probafixM1((1-k)*s_barra, -u1/(1-k),frec_inicial)
    p_mas_menos = u_mas_menos*probafixM1((1-k)*s_barra_neg, u1/(1-k),frec_inicial)
    p_menos_menos =  u_menos_menos*probafixM1((1-k)*s_barra_neg, -u1/(1-k),frec_inicial)

    Sum  = p_mas_mas+p_mas_menos+p_menos_menos+p_menos_mas
    p_mas_mas =  p_mas_mas/Sum
    p_menos_mas =  p_menos_mas/Sum
    p_mas_menos =  p_mas_menos/Sum
    p_menos_menos =  p_menos_menos/Sum
   
    return [p_mas_mas,p_mas_menos,p_menos_menos,p_menos_mas],flag 





#archivo = open('Eficiencia_u1_' +str(u1) +'_u2_' + str(u2) + '.txt','a')

def caminata_completa():
    x = [0]
    y = [0.5]
    while abs(x[-1]) < 0.05 and y[-1] < 1 and y[-1] > 0:
        P,bandera =  probabilidades(x[-1],y[-1])
        if bandera == True:
            break
        salto = np.random.choice([0,1,2,3],p = P )
        if salto == 0:
            x.append(x[-1] + u2) 
            y.append(y[-1] + u1)
        if salto == 1:
            x.append(x[-1] - u2)
            y.append(y[-1] + u1)
        if salto == 2:
            x.append(x[-1] - u2)
            if  y[-1] - u1 > 0:
                y.append(y[-1] - u1)
            else:
                 y.append(y[-1])
        if salto == 3:
            x.append(x[-1] + u2)
            if y[-1] - u1 > 0:
                y.append(y[-1] - u1)
            else:
                 y.append(y[-1])
    plt.xlim(-0.05,0.05)
    plt.ylim(0,1)
    plt.plot(x,y)
    plt.show()
    
    
caminata_completa()
