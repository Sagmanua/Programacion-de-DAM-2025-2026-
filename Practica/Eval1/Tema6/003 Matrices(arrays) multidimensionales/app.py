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
