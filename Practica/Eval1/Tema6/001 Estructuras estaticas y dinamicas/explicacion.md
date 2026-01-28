# Indroduccion brece y contexalizacion
En mi tiempo libre, disfruto mucho jugando videojuegos y viendo series anime. Estos hobbies me mantienen entretenidos mientras realizo otras actividades como nadar o seguir los partidos del fútbol.

# Desarrollo técnico correcto y preciso
## app.py
### Creo una lista de peliculas 
```
películas_favoritas=[
    "The Gentlemen",
    "Interstellar ",
    "Origen"
]
```
### imprimo esta lista
```
print(películas_favoritas)
```
### añade una nuevo valor de la lista con la `append`
```
películas_favoritas.append("Mad Max: Fury Road")
```
### imprimo esta lista
```
print(películas_favoritas)
```

### imprimo primeor valor de la lista 
```
print(películas_favoritas[0])
```
### imprimo lista usa `for`
```
for i in range(len(películas_favoritas)):
    print(películas_favoritas[i])
```

# Codigo completa

```
películas_favoritas=[
    "The Gentlemen",
    "Interstellar ",
    "Origen"
]

print(películas_favoritas)

películas_favoritas.append("Mad Max: Fury Road")

print(películas_favoritas)

print(películas_favoritas[0])

for i in range(len(películas_favoritas)):
    print(películas_favoritas[i])
```

# Cierre/Conclusión enlazando con la unidad
En este ejercicio vimos cómo crear y manipular listas en Python para organizar nuestras películas favoritas. Usando métodos como append() podemos añadir nuevos elementos de forma dinámica, acceder a elementos específicos con índices y recorrer la lista con un bucle for. Esto demuestra que las listas son una estructura muy útil para gestionar colecciones de datos