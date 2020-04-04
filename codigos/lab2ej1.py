def rbisec(fun, I, err, mit):
    """
    Funcion para aplicar algoritmo de biseccion, dando como salida
    dos listas: historial de puntos medios e historial de evaluaciones
    """
    # I = [a, b]
    a = I[0]
    b = I[1]

    # Iniciamos nuestro contador de iteraciones
    kit = 0
    
    # Iniciamos nuestras listas de puntos y evaluaciones
    hx = []
    hf = []
    
    if fun(a) * fun(b) < 0.0:
        # Si el signo de a y b son diferentes, podemos comenzar
        # Hacemos nuestra primera iteracion antes del bucle
        c = (a + b) / 2.0
        w = fun(c)
        hx.append(c)
        hf.append(w)
        while abs(w) > err and kit < mit:
            kit = kit + 1
            # Aqui elegimos a quien reemplazara nuestro punto medio
            # Sera el que mantenga la condicion inicial de a y b
            if w * fun(a) < 0.0:
                b = c
            else:
                a = c
            c = (a + b) / 2.0
            w = fun(c)
            hx.append(c)
            hf.append(w)            
    else:
        print("Elegi otro intervalo!")
            
    return hx, hf

