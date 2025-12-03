'''
    003-Utilazacion de metodos estaticos
    (c) Bohdan SYdorenko
    En nuestra actualidad digital, los videojuegos y las películas son dos de los hobbies más populares entre los jóvenes. Imagina un mundo donde estas actividades forman parte integral del día a día. 
    En este ejercicio, vamos a explorar cómo podemos utilizar objetos predeterminados en el lenguaje de programación para manejar estos hobbies.
'''
'''
Que hago


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

print(resultado)
