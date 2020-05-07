import rnewton 
import rsteff
import math

funcion = lambda x : ( math.log(x) - 1/x , 1/x + 1/x**2)

historico_newton = []
historico_steff = []

for punto_inicial in [1.39, 1.4, 1.41, 3]:
	hx_newton, _  = rnewton.rnewton(funcion, punto_inicial, 1e-6, 100)
	historico_newton.append(hx_newton)
	
	hx_steff , _ = rsteff.rsteff(funcion, punto_inicial, 1e-6, 100)
	historico_steff.append(hx_steff)

print(historico_newton)
print()
print(historico_steff) 