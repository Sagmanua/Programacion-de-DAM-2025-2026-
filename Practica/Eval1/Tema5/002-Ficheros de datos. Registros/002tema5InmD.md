# Indroduccion brece y contexalizacion
En este ejercicio, vamos a trabajar con ficheros JSON para almacenar información sobre artículos de un blog. Imagina que eres un amante de los videojuegos y te gusta leer noticias sobre anime y películas mientras disfrutas de tus juegos favoritos. Los ficheros JSON son una excelente forma de guardar y acceder a esta información.




# Desarrollo técnico correcto y preciso
## Json 
### Al primero creeo una json file con nombre `bñock.json` y gurdo informcionen ella 
```
[
  {
    "titulo": "Primer artículo",
    "fecha": "2025-10-16",
    "autor": "Jose Vicente Carratalá",
    "contenido": "Este es el contenido del primer artículo"
  },
  {
    "titulo": "Segundo artículo",
    "fecha": "2025-10-17",
    "autor": "Jose Vicente Carratalá",
    "contenido": "Este es el contenido del segundo artículo"
  }
]
```
## Python
### import `json` para puedo trabajo can json gile 
```
import json
```
### abro file json `block.json` 
```
with open("block.json", "r") as archivo:
    contenido = json.load(archivo)
```
### Muestro informacion de file `block.json`  en el terminal 
```
for articulo in contenido:
    print("####### ARTICULO ########")
    print(f"Título: {articulo['titulo']}")
    print(f"Fecha: {articulo['fecha']}")
    print(f"Autor: {articulo['autor']}")
    print(f"Contenido: {articulo['contenido']}")
    print("#########################")
    print("")
```
# Codigo completa
## Python
```
import json
with open("block.json", "r") as archivo:
    contenido = json.load(archivo)
for articulo in contenido:
    print("####### ARTICULO ########")
    print(f"Título: {articulo['titulo']}")
    print(f"Fecha: {articulo['fecha']}")
    print(f"Autor: {articulo['autor']}")
    print(f"Contenido: {articulo['contenido']}")
    print("#########################")
    print("")
```
## JSON
```
[
  {
    "titulo": "Primer artículo",
    "fecha": "2025-10-16",
    "autor": "Jose Vicente Carratalá",
    "contenido": "Este es el contenido del primer artículo"
  },
  {
    "titulo": "Segundo artículo",
    "fecha": "2025-10-17",
    "autor": "Jose Vicente Carratalá",
    "contenido": "Este es el contenido del segundo artículo"
  }
]
```

# Cierre/Conclusión enlazando con la unidad
Este ejercicio nos ha mostrado cómo los archivos JSON permiten almacenar información de manera organizada y cómo Python facilita leer y mostrar estos datos de forma clara. Trabajar con JSON nos permite acceder, modificar y gestionar información fácilmente, reforzando lo aprendido sobre ficheros y registros. En la práctica, saber manejar JSON es fundamental para procesar datos de manera eficiente y estructurada.