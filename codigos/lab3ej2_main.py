import matplotlib.pyplot as plt

# ~ from ej_2_fun_recursivo import *
# ~ from ej_2_fun_matriz import *
from ej_2_fun import *

x = [3,1,5,6]
y = [1,-3,2,4]
z = [i*0.01+1 for i in range(501)]
w = inewton(x,y,z)

plt.plot(z,w)
plt.show()
