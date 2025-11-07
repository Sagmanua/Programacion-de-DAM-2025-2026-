'''
    006-COnstructores
    (c) Bohdan SYdorenko
    En esta actividad, vamos a utilizar objetos predefinidos en Python para crear una calculadora que determine el número de cuadras necesarias basándose en el número de caballos y cuántos caballos pueden estar en cada cuadra.


'''
'''
Que hago:
1.variables
2.inputes
3.calculos 
4.imprimir todo
'''

#variables

caballos = 0
cuadra = 0

#inputes
caballos = int(input("Introduce numero de caballos"))
cuadra = int(input("introduce numero caballos por cuadra "))

#calculos
cuadra_nes = caballos // cuadra
if caballos % cuadra != 0:
    cuadra_nes += 1

print("---Resultado-----")
print("Tu tienes",caballos,"caballos")
print("en cada cuardo puede esta",cuadra,"caballos")
print("Tu nesito",cuadra_nes,"cuadras para guardar este numero de ",caballos)

