import numpy as np
from lab6ej2b import soleg
from lab6ej3 import sollu

A1 = np.array([[4,-1,0],[-1,4,-1],[0,-1,4]],dtype = float)
A2 = -np.eye(3)

A12 = np.hstack([A1,A2])
A21 = np.hstack([A2,A1])

A = np.vstack([A12,A21])

b1 = np.array([1,1,1,0,0,0], dtype = float)
b2 = np.array([1,1,1,1,1,1], dtype = float)

x11 = soleg(A,b1)
x12 = sollu(A,b1)

x21 = soleg(A,b2)
x22 = sollu(A,b2)

print(x11)
print(x12)
print(x21)
print(x22)

print(np.allclose(A @ x11, b1))
print(np.allclose(A @ x12, b1))
print(np.allclose(A @ x21, b2))
print(np.allclose(A @ x22, b2))
