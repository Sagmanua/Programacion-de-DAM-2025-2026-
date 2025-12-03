```
'''
    003-Utilazacion de metodos estaticos
    (c) Bohdan SYdorenko
    En nuestra actualidad digital, los videojuegos y las películas son dos de los hobbies más populares entre los jóvenes. Imagina un mundo donde estas actividades forman parte integral del día a día. 
    En este ejercicio, vamos a explorar cómo podemos utilizar objetos predeterminados en el lenguaje de programación para manejar estos hobbies.
'''
'''
Que hago
1.Variables
2.Asignacion de valores
3.calculos
4.imprimir todo 


'''

#Variables
tiempo_videojuegos = 0
tiempo_peliculas = 0
promedio = 0

#Asignación de valores

tiempo_peliculas =70

tiempo_videojuegos = 30

#Cálculo de la duración promedio:



def calcular_duracion_promedio(tiempo_videojuegos, tiempo_peliculas):
    promedio = (tiempo_videojuegos+tiempo_peliculas)/2
    return promedio

#dar valor 
resultado = calcular_duracion_promedio(tiempo_videojuegos,tiempo_peliculas)

#Mostrar el resultado:

print("",resultado)
```

##1.-Indroduccion brece y contexalizacion
---
En la era digital actual, los videojuegos y las películas se han convertido en dos de las actividades de ocio más populares entre los jóvenes.En este ejercicio, utilizaremos conceptos básicos de programación para representar y calcular el tiempo promedio que una persona dedica a estos hobbies, haciendo uso de objetos y funciones predeterminadas del lenguaje Python.



##2.-Desarrollo técnico correcto y preciso
---
1.Variables declarar vairiables para trabar luego con ellos
```
tiempo_videojuegos = 0
tiempo_peliculas = 0
promedio = 0
```

2.Asignacion de valores para sabar sus valor y puedo calcular sin problema
```
tiempo_peliculas =70

tiempo_videojuegos = 30
       
```
3.Hace calculos primero hacer una def para calcular en ella tiena 
```
def calcular_duracion_promedio(tiempo_videojuegos, tiempo_peliculas):
    promedio = (tiempo_videojuegos+tiempo_peliculas)/2
    return promedio

#dar valor 


```
4.dar valor en el def para calcular 
```
resultado = calcular_duracion_promedio(tiempo_videojuegos,tiempo_peliculas)
```
5.
```
imprimir todo 
```

##-3.-Aplicacion practica
---
```
#Variables
tiempo_videojuegos = 0
tiempo_peliculas = 0
promedio = 0

#Asignación de valores

tiempo_peliculas =70

tiempo_videojuegos = 30

#Cálculo de la duración promedio:



def calcular_duracion_promedio(tiempo_videojuegos, tiempo_peliculas):
    promedio = (tiempo_videojuegos+tiempo_peliculas)/2
    return promedio

#dar valor 
resultado = calcular_duracion_promedio(tiempo_videojuegos,tiempo_peliculas)

#Mostrar el resultado:

print(resultado)
```

##4.-Cierre/Conclusión enlazando con la unidad
---
En conclusión, este ejercicio permitió aplicar los conocimientos sobre el uso de variables, funciones y objetos predeterminados en Python para resolver un problema sencillo relacionado con actividades cotidianas como los videojuegos y las películas. A través del cálculo del promedio del tiempo dedicado a cada hobby, comprendimos cómo la programación puede ayudarnos a representar y analizar información del mundo real. Este tipo de prácticas refuerza los fundamentos de la unidad, fomentando el pensamiento lógico y la capacidad de modelar situaciones diarias mediante el uso de estructuras básicas del lenguaje.