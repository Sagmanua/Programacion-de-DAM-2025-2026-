import pickle
import os 
agenda = []

def menu():
    print("Seleciona una opcion")
    print("1.-Insertar una registro")
    print("2.Leer registro")
    print("3.-Guardar registros")
    print("Otro valu salir")
    opcion = input("Elige opcion")

def insertar():
    nombre = input("Dime tu nombre")
    apellidos = input("Dime tu apellidos")
    email = input("Dime tu email")
    telefono = input("Dime tu munero")
    if telefono.isdigit():
        if "@" in email:
            agenda.append([nombre,apellidos,email,telefono])
        else:
            print("eamil no tiene @")
    else:
        print("telefono es no corecta")

    

def leer():
    for i,contacto  in enumerate(agenda):
        print(i ,contacto)

def guarda():
    with open("agenda.bin","wb")as archivo:
        pickle.dump(agenda,archivo)
        archivo.close()
        print("Es gurdado en bases de datos👌")

name_file = "agenda.bin"

# Check if the file exists and is a file
if os.path.isfile(name_file):
        # Если файл существует, загружаем данные
    with open(name_file, "rb") as archivo:
        agenda = pickle.load(archivo)
    print("Datos cargados desde el archivo👌")
else:
    print("File does not exist or is not a file")


while True:
    menu()
    try:
        opcion = int(opcion)
        
        # Insertar
        if opcion == 1:
            insertar()
        #Añado a la agenda
        elif opcion == 2:
            leer()
        elif opcion == 3:
            leer()
        else:
            break
    except:
        print("This value is not number")