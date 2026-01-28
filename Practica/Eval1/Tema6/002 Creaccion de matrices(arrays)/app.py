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
