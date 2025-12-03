# Indroduccion brece y contexalizacion
En este ejercicio, vamos a mejorar nuestra gestión de clientes utilizando videojuegos como ejemplo. Imagina que cada cliente en tu sistema puede elegir su videojuego favorito. Vamos a añadir una nueva opción para buscar clientes por su videojuego preferido.




# Desarrollo técnico correcto y preciso
## Python
### Crear class `Clientes` para gurdar informacion
```
class Cliente:
    def __init__(self, nombre, edad, correo, videojuego_favorito):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.videojuego_favorito = videojuego_favorito
```
### Lista de clientes
```
clientes = []
```

### Para facil puedu muestra informcaion
```
def mostrar(self):
    print(self.nombre, "-", 
    self.edad, "años -", 
    self.correo, "-", "Juego:", 
    self.videojuego_favorito)
```
### Bucle infito con opciones
```
while True:
    print("1. Añadir cliente")
    print("2. Mostrar clientes")
    print("3. Buscar por videojuego")
    print("4. Salir")
    opcion = input("Elige una opción: ")
```
### Opcion 1 Añadir clientes
```
if opcion == "1":
    nombre = input("Nombre")
    edad = input("Edad")
    correo = input("Correo")
    juego = input("Videojuego favorito: ")
    clientes.append(Cliente(nombre, edad, correo, juego))
```
### Opcion 2 Mostrar clientes
```
elif opcion == "2":
    if not clientes:
        print("No hay clientes.")
    else:
        for c in clientes:
            c.mostrar()
```
### Opcion 3 Buscar por videojuego
```
    elif opcion == "3":
        buscar = input("Nombre del videojuego: ").lower()
        encontrados = [c for c in clientes if c.videojuego_favorito.lower() == buscar]
        if not encontrados:
            print("No se encontró ningún cliente")
        else:
            for c in encontrados:
                c.mostrar() 
```
### otro salir
```
else:
    break
```
# Codigo completa

```
class Cliente:
    def __init__(self, nombre, edad, correo, videojuego_favorito):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.videojuego_favorito = videojuego_favorito

    def mostrar(self):
        print(self.nombre, "-", 
              self.edad, "años -", 
              self.correo, "-", "Juego:", 
              self.videojuego_favorito)

clientes = []

while True:
    print("1. Añadir cliente")
    print("2. Mostrar clientes")
    print("3. Buscar por videojuego")
    print("4. Salir")
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        nombre = input("Nombre")
        edad = input("Edad")
        correo = input("Correo")
        juego = input("Videojuego favorito: ")
        clientes.append(Cliente(nombre, edad, correo, juego))
    elif opcion == "2":
        if not clientes:
            print("No hay clientes.")
        else:
            for c in clientes:
                c.mostrar()
    
    elif opcion == "3":
        buscar = input("Nombre del videojuego: ").lower()
        encontrados = [c for c in clientes if c.videojuego_favorito.lower() == buscar]
        if not encontrados:
            print("No se encontró ningún cliente")
        else:
            for c in encontrados:
                c.mostrar() 
    else:
        break
```

# Cierre/Conclusión enlazando con la unidad
En este ejercicio hemos aplicado los conceptos de clases y objetos para gestionar clientes y su videojuego favorito. Al añadir un nuevo atributo y crear funciones para agregar, mostrar y buscar clientes, vimos cómo los objetos pueden almacenar y organizar información de manera clara. Esto refuerza la utilidad de la programación orientada a objetos para modelar situaciones reales y mantener el código modular y fácil de mejorar.