# Esqueleto para completar ejercicio 1 del práctico 5, con regla del trapecio programada
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
        # Programar simpson
        pass
    else:
        print("Elegir una regla entre 'pm', 'trapecio' y 'simpson'")

    return S

