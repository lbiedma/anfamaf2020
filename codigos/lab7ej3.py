#                   A       B       curar
#medicamento 1      3       2       25

#medicamento 2      4      1       20

#total              25      10

#a) x: unidad de medicina 1
# y: unidad de medicina 2

#funcion objetivo f = 25 * x + 20 * y 

# 3 * x + 4 * y <=25
# 2 * x + y <= 10
# x,y >= 0


#b) 
# y = (25 - 3*x)/4
# y = 10 - 2* x

import numpy as np 
import matplotlib.pyplot as plt

x = np.arange(0,10,0.1)

y1 = (25 - 3*x)/4
y2 = 10 - 2* x
y3 = np.minimum(y1,y2)

plt.ylim(0,10)
plt.plot(x,y1,x,y2,x,y3)
plt.fill_between(x,0,y3)
plt.show()

#c)

c = np.array([-25, -20])
A = np.array([ [3,4], [2,1] ])
b = np.array([25,10])
x0_bounds = (0, None)
x1_bounds = (0, None)

from scipy.optimize import linprog

res = linprog(c, A_ub = A, b_ub = b, bounds=[x0_bounds, x1_bounds])
print(res)