# Esqueleto para completar ejercicio 1 del práctico 5, con reglas del trapecio y de simpson programadas
import numpy as np

def intenumcomp(fun, a, b, N, regla):
    S = None
    if regla == "pm":
        # Programar punto medio
        pass
    elif regla == "trapecio":
        puntos = N + 1
        particion = np.linspace(a, b, puntos)
        S = 0.0

        for idx in range(N):
            S = S + (fun(particion[idx]) + fun(particion[idx+1])) * (particion[idx+1] - particion[idx]) / 2.0

    elif regla == "simpson":
        if N%2 == 1:
            print("Advertencia: La regla de simpson requiere N par. Se usará N+1")
            N = N+1
        sx0 = fun(a) + fun(b)
        sx1 = 0
        sx2 = 0
        x = a
        h = (b-a)/N
        for j in range(1,N):
            x = x + h
            if j%2 == 0:
                sx2 = sx2 + fun(x)
            else:
                sx1 = sx1 + fun(x)
        S = (sx0 + 2*sx2 + 4*sx1)*h/3
    else:
        print("Elegir una regla entre 'pm', 'trapecio' y 'simpson'")

    return S

