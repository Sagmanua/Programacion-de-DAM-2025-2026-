## 1.-Indroduccion brece y contexalizacion
En este programa final del examen voy a practicar la creación de clases en Python que incluyan el método especial `__init__`, el cual permite inicializar los atributos de los objetos. Además, aprenderé a guardar información en un archivo binario utilizando la librería externa `pickle`.
Para poner en práctica estos conceptos, desarrollaré una miniaplicación CRUD (Crear, Leer, Actualizar y Eliminar), aunque en este caso solo implementaré las funciones de crear y leer clientes. De esta forma, podré almacenar y recuperar los datos automáticamente sin tener que escribirlos manualmente cada vez que se ejecute el programa.

## 2.-Desarrollo técnico correcto y preciso

### importar pikcle (si no exicte install)
```
import pickle
```
### Craer classe para puede gurdar informacion en file bin
```
class Cliente():
        def __init__(self,nombre,apellidos,email):
            self.nombre = nombre
            self.apellidos = apellidos
            self.email = email
clientes = []  
```
### aqui leido archivo los `clientes.bin` (puedo hacer esto por que tiene libliria externa pickle)
```
archivo = open("clientes.bin",'rb')
clientes = pickle.load(archivo)
archivo.close()
```
### Buckle infinito 
```
while True:
    break

```
### Usa pickle para esribir en archivo `clientes.bin` eso es puede redactar este archivo 
```
archivo=open("clientes.bin",'wb')
    pickle.dump(clientes,archivo)
    archivo.close()
```
### Muestra a usario que opciones tiene y da a el escoge un opcion
```
print("Escoge una opción:")
    print("1.-Insertar un cliente")
    print("2.-Listar clientes")
    print("3.-Salir de programa")
    opcion = int(input("Escoge una opcion:")) 
```
### opcion 1 es añado unas instancias al archivo `clientes.bin`
#### usario escribe su `nombre`,`apellidos`y`email` y todo va a gurdar en class y despues quarda en acrchivo `clientes.bin`
```
if opcion == 1:
        nombre = input("Introduce el nombre: ")
        apellidos = input("Introduce la apellido: ")
        email = input("Introduce el email: ")
        clientes.append(Cliente(nombre,apellidos,email))
```

### opcion 2 es leer al archivo `clientes.bin`
#### cada instancias tiene su idificador por eso voy mostarar con el por eso tiebe valor id en 0. Usa for para mostrar todos los clientes que tiene guardados en el archivo `clientes.bin`  (coge numero de instancias y pasar en for)
```
elif opcion == 2:
        id = 0
        for cliente in clientes:
            print("id de cliente:",id,cliente.nombre,cliente.apellidos,cliente.email)
            print()
            id += 1
```
### opcion 3 es salie de programa
#### salir de bucle infinito
```
elif opcion == 3:
        break
```
## Codigo completa

```
'''
    Exam de final tema 5 mini-Crud con pickle
    (c) Bohdan Sydorenko
'''
'''
Que hago
1.import 
2.class
3.abrir acrcivo bin 
4.bucle infinito
5.crear
6.leer
7.salir
'''

import pickle

class Cliente():
        def __init__(self,nombre,apellidos,email):
            self.nombre = nombre
            self.apellidos = apellidos
            self.email = email
clientes = []

print("mini Crud")
archivo = open("clientes.bin",'rb')
clientes = pickle.load(archivo)
archivo.close()

while True:
    archivo=open("clientes.bin",'wb')
    pickle.dump(clientes,archivo)
    archivo.close()

    print("Escoge una opción:")
    print("1.-Insertar un cliente")
    print("2.-Listar clientes")
    print("3.-Salir de programa")
    opcion = int(input("Escoge una opcion:"))
    
    if opcion == 1:
        nombre = input("Introduce el nombre: ")
        apellidos = input("Introduce la apellido: ")
        email = input("Introduce el email: ")
        clientes.append(Cliente(nombre,apellidos,email))
    elif opcion == 2:
        id = 0
        for cliente in clientes:
            print("id de cliente:",id,cliente.nombre,cliente.apellidos,cliente.email)
            id += 1
    elif opcion == 3:
        break
```

## 4.-Cierre/Conclusión enlazando con la unidad
Con la realización de este programa he podido aplicar los conocimientos aprendidos en la Unidad 5, especialmente sobre la programación orientada a objetos y el uso de persistencia de datos con la librería pickle.
A través de la creación de una clase sencilla y un pequeño sistema CRUD, comprendí cómo estructurar y gestionar objetos dentro de una lista, así como la importancia de guardar y recuperar información desde un archivo binario para mantener los datos entre ejecuciones.