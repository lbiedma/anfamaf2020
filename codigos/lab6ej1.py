import numpy as np

def soltrinf(A, b):
    n = A.shape[0]
    x = b
    
    for idx in range(n):
        for jdx in range(idx):
           x[idx] = x[idx] - A[idx, jdx] * x[jdx]
        x[idx] = x[idx] / A[idx, idx]

    return x

def soltrsup(A, b):
    n = A.shape[0]
    x = b

    for idx in range(n-1, -1, -1):
        for jdx in range(n-1, idx, -1):
            x[idx] = x[idx] - A[idx, jdx] * x[jdx]
        x[idx] = x[idx] / A[idx, idx]

    return x

