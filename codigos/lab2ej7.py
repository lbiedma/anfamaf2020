import math
import lab2ej3
import matplotlib.pyplot as plt

lista_x = []
n, h = 100, 1.5
for i in range(n+1):
	lista_x.append(i*h/n)

lista_y = []
for x in lista_x:
	fun_ = lambda y : ( y - math.exp( -(1 - x*y)**2 ), 1 - 2*x*math.exp(- (1-x*y))* (1-x*y) )
	hy, hfy = lab2ej3.rnewton(fun_ , 1.2, 1e-8, 100)
	lista_y.append(hy[-1])

plt.plot(lista_x , lista_y)
plt.show()