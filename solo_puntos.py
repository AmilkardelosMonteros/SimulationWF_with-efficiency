import numpy as np
x1 = 0.5
N = 100
def ganador(k1,s1,k0,s0):
    x = [x1]
    while x[-1] > 0 and x[-1] < 1:
        C = 0
        D = 0 
        M = 0
        while C < N:
            f = x[-1]
            print(f)
            A = np.random.binomial(1,((1+s1)*f)/((1+s1)*f+(1+s0)*(1-f)))
            D += A
            C += A*(1-k1) + (1-A)*(1-k0)
            M += 1
        x[0]=float(D)/M
    return int(float(x[-1]))

ganador(1,0.1,0,0)
def puntos(n,m,repeticiones,mu1,mu2):
    S = np.linspace(-0.5,0.5,n)
    K = np.linspace(0.3,0.7,m)
    Informacion = []
    for s in range(len(S)):
        for k in range(len(K)):
            porcentaje_ganador = 0
            for i in range(repeticiones):
                print(i)
                g = ganador(k,s,0,0)
                if g == 1:
                    porcentaje_ganador += 1/repeticiones
            Informacion.append([s,k,porcentaje_ganador])
    return Informacion

#print(puntos(3,3,5,0.01,0.1))
