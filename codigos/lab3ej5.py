import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline

# Primero, debemos leer el archivo con los datos, generando una matriz.
# La primer columna son los años, la segunda son las temperaturas que usaremos.
datos = np.loadtxt("datos_aeroCBA.dat")

# El atributo "shape" de la matriz "datos" nos dice la forma de la matriz (una tupla).
# La cantidad de filas de la matriz está en el primer elemento de shape.
filas = datos.shape[0]

# Generamos dos listas, donde vamos a colocar nuestros datos.
años = []
temps = []

# Las funciones de interpolación, en algunos casos, sólo funcionan si no tenemos NaN's,
# debemos filtrarlos usando la función de numpy "isnan".

for fila in range(filas):
    # Para acceder al elemento i,j de la matriz, debemos hacer datos[i][j]
    temperatura = datos[fila][1]
    if not np.isnan(temperatura):
        años.append(datos[fila][0])
        temps.append(temperatura)

# La función CubicSpline genera el polinomio que representa la interpolación por spline cubico.
# Necesitaremos extrapolar, por lo que podemos usar la opción extrapolate (si no se rompe al evaluar).
polinomio = CubicSpline(años, temps, extrapolate=True)

# Vamos a generar la lista de años en los que vamos a evaluar nuestro polinomio, 1957-2017.
puntos = list(range(1957, 2018))

# Evaluamos el polinomio en los puntos generados.
final = polinomio(puntos)

# Vamos a dibujar nuestro gráfico
plt.plot(puntos, final)
plt.title("Temperaturas promedio en Córdoba, 1957-2017")
plt.xlabel("Años")
plt.ylabel("Temperaturas [°C]")
plt.show()
