from lab5ej1 import intenumcomp
from math import pi, sin, sqrt

### ESQUELETO PARA RESOLVER EL EJERCICIO 6 DEL PRACTICO 5

def cociente(x, alfa):
    return 1 / sqrt(1 - sin(alfa/2)**2 * sin(x)**2)

def pendulo(long, alfa, intervalos, regla):
    """
    long: real mayor a cero que nos indique la longitud del pendulo
    alfa: numero entre 0 y 90, que indique los grados del angulo del pendulo,
    pi/2 = 90 grados ---> aplicar regla de tres simples.
    """
    
    integrando = lambda x: cociente(x, alfa)

    periodo = blabla * intenumcomp(integrando, 0, pi/2, intervalos, regla)

    return periodo
