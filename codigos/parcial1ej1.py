def fibonacci(m):
    """
    Función que retorna una lista con los primeros m elementos de la sucesión de Fibonacci
    que comienza con f_1 = 0, f_2 = 1.
    """
    assert isinstance(m, int), "Ingresar un entero"
    numeros = [] 
    if m >= 1: 
        numeros.append(0) 
    if m >= 2: 
        numeros.append(1) 
    if m >= 3: 
        for idx in range(2, m): 
            numeros.append(numeros[idx-1] + numeros[idx-2]) 
    return numeros
