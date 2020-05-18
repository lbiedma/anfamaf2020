# Ejercicio de cálculo de la función seno como integral del coseno
from math import ceil, cos
from lab5ej1 import intenumcomp

def senint(x):
    # Intervalo de longitud x, necesito una partición con intervalos de longitud < 0.01
    N = ceil(x / 0.01) + 1

    return intenumcomp(cos, 0, x, N, "trapecio")

