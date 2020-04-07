# Este código se ejecuta desde linea de comandos con 'python lib1ej4.py'
# Debido a que 0.1 no puede ser representado como una suma finita de potencias de 2,
# nunca se cumplira la condicion del while y vamos a tener que frenarlo con Ctrl + C
x = 0
while x != 10:
    x = x + 0.1
    print(x)

