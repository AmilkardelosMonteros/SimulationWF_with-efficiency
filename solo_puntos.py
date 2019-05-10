import numpy as np
import numpy as np

x1 = 0.5

N = 100

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



def puntos(n,m,repeticiones):
    S = np.linspace(-0.05,0.05,n)
    K = np.linspace(0.3,0.7,m)
    Informacion = []
    for s in S:
        for k in K:
            porcentaje_ganador = 0
            for i in range(int(repeticiones)):
                g = ganador(k,s,0,0)
                print(g)
                if g == 1:
                    porcentaje_ganador += 1/repeticiones
            Informacion.append([s,k,porcentaje_ganador])
    return Informacion

P = puntos(3,3,5.0)
