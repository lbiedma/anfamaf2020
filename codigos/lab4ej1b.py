# Este ejercicio funciona si la lista de "x" es creada como array de numpy,
# de otra forma hay que tener cuidado con la función generadora de la recta.

import matplotlib.pyplot as plt
import numpy as np

# Recta
recta = lambda x: 0.75 * x + 0.5

# Generar 20 puntos equiespaciados en [0, 10]
x_dat = np.linspace(0, 10, 20)
# Generar 20 puntos con dispersión normal en el eje y
disp = np.random.normal(size=20)
# Sumarlos a los puntos de la recta
y_dat = recta(x_dat) + disp

# Ajustar por una recta los nuevos puntos
polinomio = np.polyfit(x_dat, y_dat, deg=1)

# Graficar la recta
plt.plot(x_dat, np.polyval(polinomio, x_dat), label="ajuste")
# Graficar datos
plt.plot(x_dat, y_dat, '*', label="datos")
# Graficar recta original
plt.plot(x_dat, recta(x_dat), label="original")
plt.legend()
# Mostrar gráfico
plt.show()
