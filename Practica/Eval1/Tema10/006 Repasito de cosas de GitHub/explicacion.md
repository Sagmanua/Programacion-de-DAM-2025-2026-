# Indroduccion brece y contexalizacion
El objetivo de este ejercicio es crear un pequeño sistema para gestionar nuestras series y películas favoritas. Dado que muchas personas disfrutan de ver contenido audiovisual como entretenimiento, este programa nos permite organizar y visualizar de manera sencilla nuestras preferencias.




# Desarrollo técnico correcto y preciso
## app.py
### Declara una variable nombre_usuario para almacenar el nombre del usuario.
```
nombre_usuario = ""

```
### Declara una lista lista_series para almacenar las series favoritas del usuario.
```
lista_series = []

```
### Declara una lista lista_peliculas para almacenar las películas favoritas del usuario.
```
lista_peliculas = []

```
### Pide al usuario que ingrese su nombre y almacénalo en la variable nombre_usuario.
```
nombre_usuario = input("¡Hola! ¿Cuál es tu nombre? ")
```
### Utiliza un bucle `while` para pedir al usuario que ingrese nombres de series hasta que decida terminar.
```
def save_seria():
    while True:
        seria = input("seria")
        if seria.lower() == "fin":
            break
        elif seria.lower() == "si":
            read_seria()
        lista_series.append(seria)
```
### Si el usuario responde "Sí", muestra cada nombre de serie almacenado en la lista lista_series con un mensaje amigable.
```
elif seria.lower() == "si":
    read_seria()
```
### Utiliza un bucle `while` para pedir al usuario que ingrese nombres de series hasta que decida terminar.
```
def save_pelicula():
    while True:
        print(number)
        seria = input("seria")
        if seria.lower() == "fin":
            break
        elif seria.lower() == "si":
            read_pelicula()
        lista_series.append(seria)
def read_seria():
    for i in range (len(lista_series)):
        print(lista_series[i])

```
### Si el usuario responde "Sí", muestra cada nombre de serie almacenado en la lista lista_series con un mensaje amigable.
```
elif seria.lower() == "si":
    read_pelicula()
def read_pelicula():
    for i in range (len(lista_peliculas)):
        print(lista_peliculas[i])
```

# Codigo completa

```
nombre_usuario = ""
lista_series = []
lista_peliculas = []

nombre_usuario = input("¡Hola! ¿Cuál es tu nombre? ")
def save_seria():
    while True:
        seria = input("seria")
        if seria.lower() == "fin":
            break
        elif seria.lower() == "si":
            read_seria()
        lista_series.append(seria)
        
    

def read_seria():
    for i in range (len(lista_series)):
        print(lista_series[i])

save_seria()

def save_pelicula():
    while True:
        print(number)
        seria = input("seria")
        if seria.lower() == "fin":
            break
        elif seria.lower() == "si":
            read_pelicula()
        lista_series.append(seria)

def read_pelicula():
    for i in range (len(lista_peliculas)):
        print(lista_peliculas[i])
```

# Cierre/Conclusión enlazando con la unidad
En este ejercicio aprendimos a usar variables simples y listas para almacenar y organizar información, en este caso, sobre nuestras series y películas favoritas. Esto nos permite manejar datos de manera ordenada, agregarlos dinámicamente y mostrarlos cuando lo necesitamos.