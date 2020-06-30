from parcial2ej1a import spline_velocidad
from parcial2ej1b import trapecio_adaptativo
import matplotlib.pyplot as plt

def posicion_particula(ts, vs):
    new_ts, new_vs = spline_velocidad(ts, vs)
    
    n = len(new_ts)
    pos = [0]
    for paso in range(n-1):
        pos.append(trapecio_adaptativo(new_ts[:paso+2], new_vs[:paso+2]))
        
    plt.plot(new_ts, pos)
    plt.show()

