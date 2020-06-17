# Costo total = Costo_1 + Costo_2 + Costo_3 + Costo_4

# Costo total = Horas_1 * 68.3 + Horas_2 * 69.5 + Horas_3 * 71 + Horas_4 * 71.2

# Completar la Tarea M
# M_1 / 52 + M_2 / 57 + M_3 / 51 + M_4 / 56 >= 1

# Completar la Tarea N
# N_1 / 212 + N_2 / 218 + N_3 / 201 + N_4 / 223 >= 1

# Horas_1 = M_1 + N_1 + P_1 + Q_1

# Costo total = (M_1 + N_1 + P_1 + Q_1) * 68.3 + Horas_2 * 69.5 + Horas_3 * 71 + Horas_4 * 71.2

# Horas disponibles
# M_1 + N_1 + P_1 + Q_1 <= 220

##############

# Función objetivo: Costo total
# Restricciones:
#	Completar las tareas (4 restricciones)
#	Horas disponibles (4 restricciones)

import numpy as np
from scipy.optimize import linprog

# M_1 M_2 M_3 M_4 N_1 N_2 N_3 N_4 ... Q_4

c = np.tile(np.array([68.3, 69.5, 71, 71.2]), 4)

# Tareas

tabla = np.array([52,57,51,56,212,218,201,223,25,23,26,21,60,57,54,55])
tabla = 1/tabla

A1 = np.zeros((4,16))
I = np.repeat(np.arange(4),4)
J = np.arange(16)
A1[I,J] = -tabla

b1 = -np.ones(4)

# Horas disponibles

A2 = np.tile(np.eye(4),4)
b2 = np.array([220,300,245,190])

A_ub = np.vstack([A1,A2])
b_ub = np.hstack([b1,b2])

res = linprog(c,A_ub=A_ub,b_ub=b_ub)

# M_1 M_2 M_3 M_4 N_1 N_2 N_3 N_4 ... Q_4

x = np.round(res.x)

for i in range(4):
	print("el equipo {} debe ocupar: {}".format(i+1,x[np.arange(4)*4+i]))

#print(res)
