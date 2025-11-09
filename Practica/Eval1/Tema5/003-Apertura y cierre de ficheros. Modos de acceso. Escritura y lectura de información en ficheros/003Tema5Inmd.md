# Indroduccion brece y contexalizacion





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
