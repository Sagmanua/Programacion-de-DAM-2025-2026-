import pickle
import os 
import re

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
    nombre = input("Dime tu nombre").strip()
    apellidos = input("Dime tu apellidos").strip()
    email = input("Dime tu email").strip()
    telefono = input("Dime tu nunero").strip()
    if not check_telefono(telefono):
            print("Telefono no es correcto")
            return
    if not check_email(email):
            print("Email no tiene @")
            return

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
#---------------------------UPDATE------------------------
def actulizar():
    idx = input("Write what numero to change")
    try:
        idx = int(idx)
    except:
        print("ES no numero") 

    if 0 <= idx < len(agenda):
        nombre = input("INtroduce nombre").strip()
        apellidos = input("introduce apeelidos").strip()
        email = input("introduce eail").strip()
        telefono = input("introduce telefovo").strip()
        if not check_telefono(telefono):
            print("Telefono no es correcto")
            return
        if not check_email(email):
            print("Email no tiene @")
            return
        agenda[idx] = [nombre, apellidos, email, telefono]
        print("Registro ",idx," actualizado correctamente.")
    else:
        print("Number is not right")

#-------------------------- DELETE---------------------
def borar():
    idx = input("Write what numero to change")
    try:
        idx = int(idx)
    except:
        print("ES no numero") 
    if 0 <= idx < len(agenda):
        check_sure(idx)
    else:
        print("Number is not right")
##### Check if a have file 
def check_fiel():
    global agenda
    name_file = "agenda.bin"
    # Check if the file exists and is a file
    if os.path.isfile(name_file):
            # Если файл существует, загружаем данные
        with open(name_file, "rb") as archivo:
            agenda = pickle.load(archivo)
        print("Datos cargados desde el archivo✅")
    else:
        print("File does not exist or is not a file")

############## Check for vailido of telefono
def check_telefono(telefono):
    pattern_telefono = r"^\+?\d{1,3}[- ]?\d{2,4}([- ]?\d{2,4}){1,3}$"
    if re.fullmatch(pattern_telefono, telefono):
        return True
    else:
        return False
        
############# Check for valido of email
def check_email(email):
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.fullmatch(email_pattern, email):
        return True
    else:
        return False


#################### Check for sure
def check_sure (idx):
    print("Your sure you want delete",idx)
    opcion_segura=input("Write yes or si,if you shure")
    opcion_segura = opcion_segura.lower()
    if opcion_segura == "yes" or opcion_segura =="si":
        return True
    else:
        return False


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
        elif opcion == 4:
            actulizar()
        elif opcion == 5:
            borar()
        else:
            break
    except:
        print("This value is not number")
