import numpy as np
import matplotlib.pyplot as plt

datos = np.loadtxt("datos3b.dat")

x = datos[0,1:]
y1 = datos[1,1:]

x_hat = np.divide(1,x)
y_hat = np.divide(1,y1)

# y_hat = A + B * x_hat

p = np.polyfit(x_hat,y_hat,1)

A = p[1]
B = p[0]

fig,ax = plt.subplots(2,1)

ax[0].plot(x_hat,y_hat,'.r')
ax[0].plot(x_hat, A+B*x_hat)

ax[1].plot(x,y1,'.r')
ax[1].plot(x, np.divide(x,A*x+B))

# ax[0,0].plot(x, y1 )
# ax[1,0].plot(x[1:],y2[1:])
# ax[0,1].plot(x[3:], np.divide(1,y1[3:]) )
# ax[1,1].plot(x[1:], np.divide(1,y2[1:]))

# y = x / ( A*x + B )

# y_hat = 1 / y
# x_hat = 1 / x

# y_hat = ( A*x + B ) / ( x )
# y_hat = A + B * (1/x)

plt.show()


