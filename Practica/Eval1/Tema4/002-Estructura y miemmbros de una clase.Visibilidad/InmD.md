# Indroduccion brece y contexalizacion
Así como en los videojuegos gestionas inventarios, personajes o recursos, en programación puedes gestionar información de manera estructurada utilizando clases y objetos.
En este caso, crearemos un pequeño sistema para gestionar clientes, que nos servirá para practicar los fundamentos de la programación orientada a objetos (POO).
Igual que un juego guarda datos de jugadores (nombre, nivel, estadísticas), aquí guardaremos datos de clientes (email, nombre, dirección).




# Desarrollo técnico correcto y preciso
## Python
### Crear class `Clientes` para gurdar informacion en este clase
```
class Cliente():
    def __init__(self ):
        self.email = None
        self.nombre = None
        self.direccion = None
clientes = [] 
```
### Crear bucle infinito para hago una mini-CRUD
```
while True:
    pass
```
### Crear una introducion de mini-CRUD
```
opcion = input("Escoge una opción: ")
opcion = int(opcion)  
```
### Crear unas opcion de Insertar y Listar
```
if opcion == 1:
    print("Vamos a insertar un cliente")
    nuevocliente = Cliente()
    nuevocliente.nombre = input("Introduce el nombre del cliente: ")
    nuevocliente.email = input("Introduce el email del cliente: ")
    nuevocliente.direccion = input("Introduce la direccion del cliente: ")
    clientes.append(nuevocliente)
elif opcion == 2:
    print("Vamos a ver los clientes")
    for cliente in clientes:
        print("Nombre:", cliente.nombre)
        print("Email:", cliente.email)
    print("Dirección:", cliente.direccio
```


# Codigo completa
## Python
```
class Cliente():
    def __init__(self ):
        self.email = None
        self.nombre = None
        self.direccion = None

clientes = []  

while True: 
    print("Selecciona una opción: ")
    print("1.-Insertar un cliente")
    print("2.-Listar clientes")

    opcion = input("Escoge una opción: ")
    opcion = int(opcion)   
  
    if opcion == 1:
        print("Vamos a insertar un cliente")

        nuevocliente = Cliente()
        nuevocliente.nombre = input("Introduce el nombre del cliente: ")
        nuevocliente.email = input("Introduce el email del cliente: ")
        nuevocliente.direccion = input("Introduce la direccion del cliente: ")
        clientes.append(nuevocliente)
    elif opcion == 2:
        print("Vamos a ver los clientes")
        for cliente in clientes:
            print("Nombre:", cliente.nombre)
            print("Email:", cliente.email)
            print("Dirección:", cliente.direccion)

```

## Cierre/Conclusión enlazando con la unidad
Este ejercicio demuestra cómo la programación orientada a objetos permite manejar información estructurada de manera clara y reutilizable.
Así como un videojuego usa clases para representar personajes o enemigos, nosotros usamos la clase Cliente para representar entidades con atributos propios.
Comprender este concepto es clave para proyectos más grandes, como sistemas de usuarios en juegos, plataformas de streaming de anime o bases de datos de películas.
De esta forma, la POO se convierte en una herramienta útil tanto en el ámbito profesional como en tus hobbies digitales.