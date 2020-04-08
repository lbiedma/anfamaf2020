funcion = lambda x : 2**(x-1)

from lab2ej5 import ripf

hx  = ripf(funcion, 1.5, 1e-5, 100)

print(hx)