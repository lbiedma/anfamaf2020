import math

def mala(a, b, c):
    """
    Función para obtener las dos raíces de un polinomio de grado 2 de la forma
    a * x^2 + b * x + c, usando la fórmula del discriminante "mala".
    
    La salida de esta función son dos números, x_1 y x_2, formando una tupla.
    
    Para poder obtener ambos elementos, hay que llamar a esta función de la forma:
        x_1, x_2 = mala(a, b, c)
    """
    
    x_1 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    
    x_2 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    
    return x_1, x_2
    
    
def buena(a, b, c):
    """
    Función para obtener las dos raíces de un polinomio de grado 2 de forma "buena",
    evitando posibles errores de cancelación por operacion es de punto flotante.
    
    La salida de esta función son dos números, x_1 y x_2, formando una tupla.
    
    Para poder obtener ambos elementos, hay que llamar a esta función de la forma:
        x_1, x_2 = buena(a, b, c)
    """
    
    # Dependiendo del signo de b, elegiremos como primera raíz la que nos deja "más lejos del 0"
    if b >= 0:
        x_1 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    
    else:
        x_1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        
    # Una vez obtenida la primera raíz, recordemos que x_1*x_2 = c/a y usamos eso para obtener x_2
    
    x_2 = c / (a * x_1)
    
    return x_1, x_2    
    
