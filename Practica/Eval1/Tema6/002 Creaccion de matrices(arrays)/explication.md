# Indroduccion brece y contexalizacion
En mi tiempo libre, disfruto mucho jugando videojuegos y viendo series anime y películas. Estos hobbies me mantienen entretenidos y ayudan a relajarme después del día. Hoy vamos a crear un programa que nos permita gestionar nuestro menú de comidas favoritas, similar al que usamos para ver nuestros animes favoritos.Este programa nos permitirá crear un menú personal de comidas, agregar nuevos platos, listarlos y guardarlos en un archivo binario para consultarlos más tarde. Esto combina la diversión de organizar listas con la práctica de programación que estamos aprendiendo en clase.

# Desarrollo técnico correcto y preciso
## Python
### import `picke` y `os` para este 
```
import pickle
import os
```
### crear una array de la menu comida
```
menu_comidas = []
```
### creo funcion para demuestra de menu de aplicacion
```
def mostrar_menu():
    print("«Selecciona» una opción")
    print("1.-Introducir nueva comida")
    print("2.-Listar comidas")
    print("3.-Guardar menú")
    print("4.-Actualizar comida")
    print("5.-Borrar comida")
    print("Otro valor para salir")
```
### hago la inserto de `menu_comidas`
#### da a usario escribir que su quieo inserta con `input`  y con `append`guarda en la `menu_comida`
```
def insertar_comida():
    nombre = input("Introduce el nombre de la comida: ").strip()
    descripcion = input("Introduce la descripción de la comida: ").strip()
    precio = input("Introduce el precio de la comida: ").strip()
    menu_comidas.append([nombre, descripcion, precio])
```
### leido de la menu 
#### usa la for para imprimir cada guardocion en nuevo linia 
```
def listar_comidas():
    for i, comida in enumerate(menu_comidas):
        print(i, comida)
```
### gurdar menu en la bin file 
#### al principio probar puede gurdar si no paso error usa `tyr` y `exept`
#### usa picke para gurdar array `menu_comidas`de la en file bin si paso bien sale mensaje 
```
def guardar_menu():
    try:
        with open("menu.bin","wb") as archivo:
            pickle.dump(menu_comidas, archivo)
        print("Menú guardado correctamente ✅")
    except:
        print("No se pudo guardar el archivo")
```

### carga la archivo bin 
#### hace gloabl array `menu_comidas` para trabajar con ella
#### en esto caso uso `if` y `esle` para vojer mensaje 
#### en if probar cargar file `menu.bin` con la pickle y gurdar en la array `menu_comidas`
```
def cargar_menu():
    global menu_comidas
    if os.path.isfile("menu.bin"):
        with open("menu.bin", "rb") as archivo:
            menu_comidas = pickle.load(archivo)
        print("Menú cargado desde archivo ✅")
    else:
        print("No existe un menú guardado")
```
### antes de hace bucle infinito hace funcion `cargar_menu`
### hace bucle infinito y da a user probar eliger que su qiere hacer.Bucle tiene `try` y `Except` si usario paso no int applicacion no falta solo da error.En la try tiene menu 
```
while True:
    mostrar_menu()
    opcion = input("Elige opción: ")
    try:
        opcion = int(opcion)
        if opcion == 1:
            insertar_comida()
        elif opcion == 2:
            listar_comidas()
        elif opcion == 3:
            guardar_menu()
        else:
            break
    except:
        print("Valor no válido")
```

# Codigo completa
## app-py
```
import pickle
import os

menu_comidas = []

def mostrar_menu():
    print("«Selecciona» una opción")
    print("1.-Introducir nueva comida")
    print("2.-Listar comidas")
    print("3.-Guardar menú")
    print("4.-Actualizar comida")
    print("5.-Borrar comida")
    print("Otro valor para salir")

#------------------INSERTAR COMIDA-----------------
def insertar_comida():
    nombre = input("Introduce el nombre de la comida: ").strip()
    descripcion = input("Introduce la descripción de la comida: ").strip()
    precio = input("Introduce el precio de la comida: ").strip()
    menu_comidas.append([nombre, descripcion, precio])

#------------------LEER COMIDAS-------------------
def listar_comidas():
    for i, comida in enumerate(menu_comidas):
        print(i, comida)

#------------------GUARDAR MENU-------------------
def guardar_menu():
    try:
        with open("menu.bin","wb") as archivo:
            pickle.dump(menu_comidas, archivo)
        print("Menú guardado correctamente ✅")
    except:
        print("No se pudo guardar el archivo")




#------------------CARGAR MENU EXISTENTE-------------
def cargar_menu():
    global menu_comidas
    if os.path.isfile("menu.bin"):
        with open("menu.bin", "rb") as archivo:
            menu_comidas = pickle.load(archivo)
        print("Menú cargado desde archivo ✅")
    else:
        print("No existe un menú guardado")

#------------------BUCLE PRINCIPAL------------------
cargar_menu()
while True:
    mostrar_menu()
    opcion = input("Elige opción: ")
    try:
        opcion = int(opcion)
        if opcion == 1:
            insertar_comida()
        elif opcion == 2:
            listar_comidas()
        elif opcion == 3:
            guardar_menu()
        else:
            break
    except:
        print("Valor no válido")

```

# Cierre/Conclusión enlazando con la unidad
Este ejercicio nos permite aplicar conceptos vistos en clase, como:

Uso de listas para almacenar información.

Funciones para organizar el código.

Manejo de archivos binarios con pickle para guardar datos de forma permanente.

Además, muestra cómo podemos integrar nuestros hobbies (como organizar series o comidas favoritas) en la programación, haciendo el aprendizaje más divertido y práctico. En futuras tareas, estos conceptos pueden extenderse a crear programas más complejos, como agendas, colecciones de películas o juegos favoritos, o incluso menús interactivos más elaborados.