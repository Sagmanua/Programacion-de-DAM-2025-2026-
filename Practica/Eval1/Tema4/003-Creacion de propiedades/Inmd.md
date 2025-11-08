# Indroduccion brece y contexalizacion
En nuestra sociedad actual, las series anime y las películas son una fuente de entretenimiento muy popular. Muchos jóvenes disfrutan de coleccionables y productos relacionados con sus franquicias favoritas. En este ejercicio, combinaremos este interés con la programación orientada a objetos, creando una aplicación simple para gestionar productos personalizados.

# Desarrollo técnico correcto y preciso
### Crear class `Productos` para gurdar informacion en este clase
```
class Productos():
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
```
### Guardo una informacion en classe 
```
producto = Productos("Squishy", 15, ["Juguetes"])
```
### Crear bucle infinito para hago una mini-CRUD
```
while True:
    pass
```
### Crear una introducion de mini-CRUD
```
print("\n1. Ver detalles del producto")
print("2. Agregar categoría")
opcion = int(input("Elige una opción: "))
```
### Crear unas opcion de Insertar y Listar
```
if opcion == 1:
    print("\nNombre:", producto.nombre)
    print("Precio:", producto.precio)
    print("Categorías:", producto.categoria)
elif opcion == 2:
    nuevocategoria = input("Escribe nueva categoría: ")
    producto.categoria.append(nuevocategoria)
else:
    break
```

# Codigo completa
## Python
```
class Productos():
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

producto = Productos("Squishy", 15, ["Juguetes"])

print("Categorías actuales del producto:", producto.categoria)

while True:
    print("\n1. Ver detalles del producto")
    print("2. Agregar categoría")
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        print("\nNombre:", producto.nombre)
        print("Precio:", producto.precio)
        print("Categorías:", producto.categoria)
    elif opcion == 2:
        nuevocategoria = input("Escribe nueva categoría: ")
        producto.categoria.append(nuevocategoria)
    else:
        break
```
# Cierre/Conclusión enlazando con la unidad
Con este ejercicio hemos aprendido a crear una clase con propiedades y a instanciar objetos en Python. También hemos visto cómo leer y modificar listas dentro de un objeto y cómo usar estructuras condicionales if para interactuar con el usuario. Esto sirve como base para desarrollar aplicaciones más complejas de gestión de productos, similares a tiendas en línea o colecciones de artículos de anime, mostrando cómo la programación orientada a objetos se aplica en la vida real.