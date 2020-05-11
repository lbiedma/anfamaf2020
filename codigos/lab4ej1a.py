# Instrucciones para resolver el ejercicio 1 del práctico 4
import matplotlib.pyplot as plt
import numpy as np

# Revisar bien dónde están los datos que queremos importar
datos = np.loadtxt("../datos/datos1a.dat")

# Los datos tendrán los "x" en el primer elemento y los "y" en el segundo del arreglo
x_dat = datos[0]
y_dat = datos[1]

# np.polyfit devuelve el polinomio de grado k que cumpla el ajuste por cuadrados mínimos
# Realizar el ajuste con una recta implica buscar el polinomio de grado 1
polinomio = np.polyfit(x_dat, y_dat, deg=1)

plt.plot(x_dat, y_dat, '*', label="datos")
# Evaluar usando np.polyval
plt.plot(x_dat, np.polyval(polinomio, x_dat), label="ajuste")
plt.legend()
plt.show()

