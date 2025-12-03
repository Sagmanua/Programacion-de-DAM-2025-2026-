import sys

argumentos = sys.argv
nombre = argumentos[1]
edad = argumentos[2]
entero = int(edad)
doble = entero*2
print("Hola",nombre,"edad double",+str(doble)+"años")