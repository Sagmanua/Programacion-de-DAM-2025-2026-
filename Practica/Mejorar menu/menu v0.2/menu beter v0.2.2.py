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
    if not is_numeric(idx):
        print("Number is not numeric")
        return 
    if 0 <= idx < len(agenda):
        nombre = input("INtroduce nombre")
        apellidos = input("introduce apeelidos")
        email = input("introduce eail")
        telefono = input("introduce telefovo")
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
    idx = input("Write what numero to delete")
    try:
        idx = int(idx)
        if 0 <= idx < len(agenda):
            print("Your shure you want delete",idx)
            opcion_segura=input("Write yes or si,if you shure")
            opcion_segura = opcion_segura.lower()
            if opcion_segura == "yes" or opcion_segura =="si":
                agenda.pop(idx)
    except ValueError:
        print("number is not numeric")
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

############## Check for number is numerico
def check_num(idx,opcion):
    if idx == int(idx) or opcion == int(opcion):
        return True
    else:
        return False
#################### Check for sure
def check_sure ():
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
