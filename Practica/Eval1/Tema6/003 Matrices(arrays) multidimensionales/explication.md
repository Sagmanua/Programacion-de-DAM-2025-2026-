# Indroduccion brece y contexalizacion

En un mundo lleno de diversión y entretenimiento, los videojuegos son una parte importante de muchas personas. Para este ejercicio, vamos a imaginar que estás jugando a uno de tus juegos favoritos mientras te sumerges en el universo del anime y las películas que tanto disfrutas. Imagina que cada vez que completes un nivel o termine una serie, quieres guardar tu progreso o anotar algo interesante sobre lo que acabaste de ver.



# Desarrollo técnico correcto y preciso
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
## app.py
```
import pickle
import os 

agenda = []

def menu():
    print("«Selecciona» una opcion")
    print("1.-Insertar una registro")
    print("2.-Leer registro")
    print("3.-Guardar registros")
    print("Otro valu salir")
############# WRITE 
def insertar():
    nombre = input("Dime tu nombre").strip()
    apellidos = input("Dime tu apellidos").strip()
    email = input("Dime tu email").strip()
    telefono = input("Dime tu nunero").strip()


    agenda.append([nombre,apellidos,email,telefono])
#--------------------READ
def leer():
    for i,contacto  in enumerate(agenda):
        print(i ,contacto)
#---------------------------SAVE-----------------------------
def guarda():
    try:
        with open("agenda.bin","wb")as archivo:
            pickle.dump(agenda,archivo)
            archivo.close()
            print("Es guardado en bases de datos👌")
    except:
        print("File cant save")



##### Check if a have file 
def check_fiel():
    global agenda
    name_file = "agenda.bin"
    if os.path.isfile(name_file):
        with open(name_file, "rb") as archivo:
            agenda = pickle.load(archivo)
        print("Datos cargados desde el archivo✅")
    else:
        print("File does not exist or is not a file")






############## Bucle infinito
check_fiel()
while True:
    
    menu()
    opcion = input("Elige opcion")
    try:
        opcion = int(opcion)
        if opcion == 1:
            insertar()
        elif opcion == 2:
            leer()
        elif opcion == 3:
            guarda()
            break
    except:
        print("This value is not number")

```

# Cierre/Conclusión enlazando con la unidad
Este ejercicio no solo te ayuda a practicar listas, diccionarios y archivos binarios en Python, sino que también demuestra cómo estas herramientas pueden servir para organizar información real, igual que llevar un registro de tus avances en tus videojuegos o animes favoritos.