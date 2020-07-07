import numpy as np
from lab6ej1 import soltrinf

def sor(A,b,omega,err,mit):
	L = np.tril(A,-1)
	D = np.diag(np.diag(A))
	U = np.triu(A,1)
	M = D + omega*L
	N = omega*U + (omega-1)*D
	n = b.shape[0]
	x = np.zeros(n)
	for i in range(mit):
		xn = soltrinf(M, omega*b - N @ x)
		if np.linalg.norm(xn-x,ord=np.inf) <= err:
			return [xn,i+1]
		x = xn.copy()
	return [x,mit]
