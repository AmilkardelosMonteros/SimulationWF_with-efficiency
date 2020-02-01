import numpy as np
import matplotlib.pyplot as plt

u1 = 0.01 #Incremento en K (y)

u2 = 0.1 #Incremento en S (x)
frec_inicial = 0.5
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
    if abs(s_barra) > 5:
        print('S_gorro salio!!')
        return [0.25,0.25,0.25,0.25],True
    
    p_mas_mas  = probafixWF(s_barra,frec_inicial)
    p_menos_mas = p_mas_mas 
    p_menos_menos = probafixWF(s_barra_neg,frec_inicial)
    p_mas_menos =  p_menos_menos
    Sum  = p_mas_mas+p_mas_menos+p_menos_menos+p_menos_mas
    p_mas_mas =  p_mas_mas/Sum
    p_menos_mas =  p_menos_mas/Sum
    p_mas_menos =  p_mas_menos/Sum
    p_menos_menos =  p_menos_menos/Sum
    return [p_mas_mas,p_mas_menos,p_menos_mas,p_menos_menos],flag 

archivo = open('Exp2_s_5_frec_0.5.txt','w')

def caminata():
    x = 0
    y = 0.5
    while abs(x) < 5 and y < 1 and y > 0:
        P,bandera =  probabilidades(x,y)
        if bandera == True:
            break
        salto = np.random.choice([0,1,2,3],p = P)
        if salto == 0:
            y = y + u1
            x = x + u2
        if salto == 1:
            y = y + u1
            x = x - u2
        if salto == 2:
            y = y - u1
            x = x + u2
        if salto == 3:
            y = y - u1
            x = x - u2
    np.savetxt(archivo,np.matrix([x,y]))

for i in range(500):
    if i%10:
        print(i)
    caminata()

archivo.close()
def caminata_completa():
    x = [0]
    y = [0.5]
    while abs(x[-1]) < 5 and y[-1] < 1 or y[-1] > 0:
        P,bandera =  probabilidades(x[-1],y[-1])
        if bandera == True:
            break
        salto = np.random.choice([0,1,2,3],p = P )
        if salto == 0:
            y.append(y[-1] + u1)
            x.append(x[-1] + u2) 
        if salto == 1:
            y.append(y[-1] + u1)
            x.append(x[-1] - u2)
        if salto == 2:
            y.append(y[-1] - u1)
            x.append(x[-1] + u2)
        if salto == 3:
            y.append(y[-1] - u1)
            x.append(x[-1] - u2)
    plt.xlim(-5,5)
    plt.ylim(0,1)
    plt.plot(x,y)
    plt.show()

