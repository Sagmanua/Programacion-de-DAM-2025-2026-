# Indroduccion brece y contexalizacion





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
