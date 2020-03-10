# Importar librerías que vayamos a utilizar en primera instancia
import random

def vander(n,m):
    """
    Función que imprime los valores de una matriz de Vandermonde de dimensión n x m.
    Atención: No devuelve la matriz, sólo imprime en pantalla los valores. Vamos a hacer
    álgebra lineal y trabajar con matrices unos prácticos más adelante.
    """
    for idx in range(1, n+1):
        for jdx in range(1, m+1):
            print("A({},{}) = {}".format(idx, jdx, 1/(idx+jdx)))
            


def suma_aleatorio(n):
    """
    Función que suma números aleatorios hasta que la suma da mayor o igual que n.
    """
    suma = 0
    
    while suma < n:
        # aca voy a sumar un numero aleatorio
        suma = suma + random.random()
        print(suma)

    return suma

