import random

def vander(n,m):

    for idx in range(1, n+1):
        for jdx in range(1, m+1):
            print("A({},{}) = {}".format(idx, jdx, 1/(idx+jdx)))
            


def suma_aleatorio(n):
    
    suma = 0
    
    while suma < n:
        # aca voy a sumar un numero aleatorio
        suma = suma + random.random()
        print(suma)

