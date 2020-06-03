import numpy as np

def jacobi(A,b,err,mit):

    n = A.shape[0]
    x = np.zeros(n)
    x_n = np.zeros(n)
    k = 0
    while k < mit:
        for i in range(n):
            s = 0
            for j in range(n):
                if j != i:
                    s = s + A[i,j] * x[j]
        
            x_n[i] = (b[i]-s)/A[i,i]
        
        if np.linalg.norm(x_n - x, np.inf) <= err:
            print('La norma infinito de la diferencia es menor que la tolerancia dada')
            return x_n,k
        
        x = x_n
        x_n = np.zeros(n)
        k+=1
        
    return x, ks