# Indroduccion brece y contexalizacion
En este ejercicio, he decidido combinar dos de mis hobbies favoritos: videojuegos y series/anime. Para ello, crearé un archivo donde almacenaré mi nombre de usuario y mis videojuegos favoritos, tal como si fuera un pequeño registro personal de mis intereses. Esto me permitirá practicar cómo leer y escribir información en archivos usando los modos que hemos estudiado en clase.

# Desarrollo técnico correcto y preciso
## Python 
### declaro variable de nobre de archivo
```
nombre_archivo = "videojuegos.txt"
```
### Escribo mi nobre en acricvo  
```
with open(nombre_archivo, "w") as archivo:
    archivo.write("Usario\n")  
```
### Esrico mis juegos favoritos
```
with open(nombre_archivo, "a") as archivo:
    archivo.write("The Legend of Zelda\n\n")
    archivo.write("Minecraft\n\n")
    archivo.write("Super Mario Odyssey\n\n")
    archivo.write("Halo Infinite\n\n")  # Puedes añadir más si quieres
```
### leido este archivo y muestro todo en terminal
```
with open(nombre_archivo, "r") as archivo:
    contenido = archivo.read()
    print(contenido)
```


# Codigo completa

```
nombre_archivo = "videojuegos.txt"

with open(nombre_archivo, "w") as archivo:
    archivo.write("Bohdan\n")  

with open(nombre_archivo, "a") as archivo:
    archivo.write("The Legend of Zelda\n\n")
    archivo.write("Minecraft\n\n")
    archivo.write("Super Mario Odyssey\n\n")
    archivo.write("Halo Infinite\n\n")  # Puedes añadir más si quieres

with open(nombre_archivo, "r") as archivo:
    contenido = archivo.read()
    print(contenido)

```

# Cierre/Conclusión enlazando con la unidad
Este ejercicio me permitió aplicar de manera práctica los modos de apertura de archivos que hemos estudiado: "w" para crear y sobrescribir, "a" para añadir información, y "r" para leer contenido. Además, me ayudó a organizar y registrar de manera sencilla mis hobbies, demostrando cómo la programación puede integrarse con intereses personales de forma práctica.