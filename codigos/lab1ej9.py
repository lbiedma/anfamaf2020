def horn(coefs, x0):
    """
    Funcion para evaluar polinomios en un punto utilizando
    el algoritmo de Horner.
    """
    # coefs = [1, 2, 3] --->  p(x) = x^2 + 2x + 3

    n = len(coefs)
    b = coefs[0]
    for idx in range(1,n):
        b = coefs[idx] + b * x0

    return b

