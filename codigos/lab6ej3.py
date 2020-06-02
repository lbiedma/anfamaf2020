from scipy.linalg import lu
from lab6ej1 import soltrinf, soltrsup

def sollu(A,b):
	P,L,U = lu(A)
	y = soltrinf(L,P.T @ b)
	x = soltrsup(U,y)
	return x
