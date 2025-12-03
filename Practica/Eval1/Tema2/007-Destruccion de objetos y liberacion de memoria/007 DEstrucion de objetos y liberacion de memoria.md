```
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
```
##1.-Indroduccion brece y contexalizacion
---
En la gestión de establos, es importante saber cuántas cuadras se necesitan para alojar a todos los caballos. Este ejercicio desarrollará una calculadora en Python que, con el número total de caballos y la capacidad de cada cuadra, determine automáticamente las cuadras necesarias usando solo funciones predefinidas del lenguaje.



##2.-Desarrollo técnico correcto y preciso
---

1.Declaramos variables para trabajar con ellos luego 
```
caballos = 0
cuadra = 0
```

2.inputes da a usario introduce su valor de caballos y cudrados
```
caballos = int(input("Introduce numero de caballos"))
cuadra = int(input("introduce numero caballos por cuadra "))
       
```
3.calculos con valor que usario nos da 
```
cuadra_nes = caballos // cuadra
if caballos % cuadra != 0:
    cuadra_nes += 1
```
4.imprimir todo los tados que usario nos da y imprimir calculos que programa hace 
```
print("---Resultado-----")
print("Tu tienes",caballos,"caballos")
print("en cada cuardo puede esta",cuadra,"caballos")
print("Tu nesito",cuadra_nes,"cuadras para guardar este numero de ",caballos)

```


##-3.-Aplicacion practica
---
```
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
```

##4.-Cierre/Conclusión enlazando con la unidad
---
La calculadora de cuadras permite aplicar conceptos básicos de programación, como la entrada de datos, operaciones aritméticas y estructuras condicionales, para resolver un problema práctico. Este ejercicio refuerza la comprensión de cómo usar objetos y métodos predefinidos en Python, mostrando cómo la teoría de la unidad se traduce en soluciones concretas para situaciones reales.