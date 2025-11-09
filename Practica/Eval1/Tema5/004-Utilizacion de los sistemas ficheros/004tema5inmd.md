# Indroduccion brece y contexalizacion
En este contexto, estamos trabajando con los sistemas de ficheros, una parte crucial de cualquier sistema informático. A través de ejercicios prácticos, aprenderás a listar el contenido de una carpeta, recorrer directorios y manejar archivos en Python. Además, como aficionado a las series anime, te proponemos un ejercicio divertido que involucra buscar elementos específicos dentro de un archivo.

# Desarrollo técnico correcto y preciso
## Python Parte 1 
### import `os` para puedo operate con sistema operativa 
```
import os
```
### usario puedo escibir ruta a su propia carpeta
```
carpeta = input("Indica una carpeta: ")
```
### hace listo de arvivo 
```
elementos = os.listdir(carpeta)
```
### Muestro todo 
```
for elemento in elementos:
    ruta = os.path.join(carpeta, elemento)
    print(ruta)
```
## Python parte 2 
### usario puedo escibir ruta a su propia carpeta
```
carpeta = input("Indica una carpeta: ")
```
### Muestro todo 
```
for directorio,carpetas,archivo in os.walk(carpeta):
    print(directorio)
    print(carpetas)
    print(archivo)
```
## Python Parte 3 
### Abrir archivo `mapa.txt` en que guardado ruta todos archivos en la carpeta Github 
```
archivo = open("mapa.txt",'r') # READ
```
### Introduce palabra para buscar
```
busca = input("Introduce el término a buscar: ")
```
### Muestro todo
```
lineas = archivo.readlines()

for linea in lineas:
    if busca in linea:
        print("###########################")
        print("Encontrado!: ",linea)   
```
# Codigo completa

```
import os

# Parte 1
carpeta = input("Indica una carpeta: ")

elementos = os.listdir(carpeta)

for elemento in elementos:
    ruta = os.path.join(carpeta, elemento)
    print(ruta)

# Parte 2
carpeta = input("Indica una carpeta: ")

for directorio,carpetas,archivo in os.walk(carpeta):
    print(directorio)
    print(carpetas)
    print(archivo)

# Parte 3 
archivo = open("mapa.txt",'r') # READ
busca = input("Introduce el término a buscar: ")

lineas = archivo.readlines()

for linea in lineas:
    if busca in linea:
        print("###########################")
        print("Encontrado!: ",linea)   


```

# Cierre/Conclusión enlazando con la unidad
En esta práctica hemos aplicado los conceptos fundamentales de los sistemas de ficheros: listar carpetas, recorrer directorios y buscar información en archivos. Estas acciones reflejan cómo organizar y acceder a datos de forma estructurada. Al relacionarlo con series anime y videojuegos, podemos ver aplicaciones reales, como gestionar episodios o buscar personajes favoritos en archivos. Así, consolidamos la teoría de la unidad de sistemas de ficheros de manera práctica y útil.