import numpy as np

def egauss(A, b):
    n = A.shape[0]
    U = A.copy()
    y = b.copy()

    for k in range(n-1):
        for i in range(k+1, n):
            if U[k, k] == 0:
                print("Elemento de la diagonal cero: {}, {}".format(k, k))
                return None
            m = U[i, k] / U[k, k]

            for j in range(k+1, n):
                U[i, j] = U[i, j] - m * U[k, j]
            y[i] = y[i] - m * y[k]

    U = np.triu(U)

    return U, y
