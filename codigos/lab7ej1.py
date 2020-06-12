# cantidad_P >= 3
# cantidad_N >= 1.5
# cantidad_K >= 4

#		P	N	K	$
# T1	3	1	8	10
# T2	2	3	2	8

# x : Kg de fertilizante T1 en 1 Kg de fertilizante Nuevo
# y : Kg de fertilizante T2 en 1 Kg de fertilizante Nuevo

# x + y = 1

# minimizar el costo total cubriendo requerimientos del suelo

# Costo total de 1 Kg de fertilizante Nuevo: x*10 + y*8

# Requerimientos:
# x*3 + y*2 >= 3
# x + 3*y >= 1.5
# x*8 + y*2 >= 4

# min 10*x+8*y
# s.a
#	 x*3 + y*2 >= 3
#	 x + 3*y >= 1.5
#	 x*8 + y*2 >= 4

# y >= (3 - 3*x)*(1/2)
# y >= (1.5 - x)*(1/3)
# y >= (4 - 8*x)*(1/2)

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,1.01,0.01)

y1 = (3 - 3*x)*(1/2)
y2 = (1.5 - x)*(1/3)
y3 = (4 - 8*x)*(1/2)

y4 = np.maximum(y1,np.maximum(y2,y3))

plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)

plt.fill_between(x,y4,2.5,alpha=0.5)

#plt.fill_between(x,y1,2.5,alpha=0.,hatch='/')
#plt.fill_between(x,y2,2.5,alpha=0.,hatch='|')
#plt.fill_between(x,y3,2.5,alpha=0.,hatch='-')

plt.ylim(0,2.5)
plt.xlim(0,1)

plt.grid()

plt.show()
