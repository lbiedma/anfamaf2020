from ej3a import *

n = 2
error = error_cos([0,1],n)

while error > 10**-6:
	n+=1
	error = error_cos([0,1],n)

print("La cantidad de puntos necesaria es {}".format(n))
