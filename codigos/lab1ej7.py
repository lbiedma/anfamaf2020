from lab1ej7fun import potencia

print("Ingrese un número entero: ",end='')
x=int(input())

for i in range(1,6):
	print(potencia(x,i))
