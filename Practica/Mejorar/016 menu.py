import pickle
import os 
agenda = []

def menu():
    print("«Selecciona» una opcion")
    print("1.-Insertar una registro")
    print("2.-Leer registro")
    print("3.-Guardar registros")
    print("4.-Aclulizar registros")
    print("5.-borar regustro")
    print("Otro valu salir")
############# WRITE 
def insertar():
    nombre = input("Dime tu nombre")
    apellidos = input("Dime tu apellidos")
    email = input("Dime tu email")
    telefono = input("Dime tu nunero")
    if telefono.isdigit():
        if "@" in email:
            agenda.append([nombre,apellidos,email,telefono])
        else:
            print("eamil no tiene @")
    else:
        print("telefono es no corecta")
############ READ
def leer():
    for i,contacto  in enumerate(agenda):
        print(i ,contacto)
############ SAVE
def guarda():
    with open("agenda.bin","wb")as archivo:
        pickle.dump(agenda,archivo)
        archivo.close()
        print("Es guardado en bases de datos👌")
############# UPDATE
def actulizar():
    idx_actual = input("Write what numero to change")
    try:
        idx_actual = int(idx_actual)
        if 0 <= idx_actual < len(agenda):
            nombre_actual = input("INtroduce nombre")
            apellidos_actual = input("introduce apeelidos")
            email_actual = input("introduce eail")
            telefono_actual = input("introduce telefovo")
            if telefono_actual.isdigit():
                if "@" in email_actual:
                    agenda[idx_actual] = [nombre_actual, apellidos_actual, email_actual, telefono_actual]
                else:
                    print("eamil no tiene @")
            else:
                print("telefono es no corecta")
        else:
            print("Number is not right")
    except ValueError:
        print("number is not numeric ")
########### DELETE
def borar():
    idx_borar = input("Write what numero to delete")
    try:
        idx_borar = int(idx_borar)
        if 0 <= idx_borar < len(agenda):
            print("Your shure you want delete",idx_borar)
            opcion_segura=input("Write yes or si")
            if opcion_segura == "yes" or opcion_segura =="si":
                agenda.pop[idx_borar]
    except ValueError:
        print("number is not numeric")
def check_fiel():
    global agenda
    name_file = "agenda.bin"
    # Check if the file exists and is a file
    if os.path.isfile(name_file):
            # Если файл существует, загружаем данные
        with open(name_file, "rb") as archivo:
            agenda = pickle.load(archivo)
        print("Datos cargados desde el archivo👌")
    else:
        print("File does not exist or is not a file")

check_fiel()
while True:
    menu()
    opcion = input("Elige opcion")
    try:
        opcion = int(opcion)
        
        # Insertar
        if opcion == 1:
            insertar()
        #Añado a la agenda
        elif opcion == 2:
            leer()
        elif opcion == 3:
            guarda()
        elif opcion == 4:
            actulizar()
        elif opcion == 5:
            borar()
        else:
            break
    except:
        print("This value is not number")