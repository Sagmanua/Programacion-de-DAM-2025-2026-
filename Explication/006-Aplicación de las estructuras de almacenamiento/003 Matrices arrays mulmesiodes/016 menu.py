import pickle
agenda = []

while True:
    print("Seleciona una opcion")
    print("1.-Insertar una registro")
    print("2.Leer registro")
    print("3.-Guardar registros")
    opcion = int(input("Elige opcion"))
    # Insertar
    if opcion == 1:
        nombre = input("Dime tu nombre")
        apellidos = input("Dime tu apellidos")
        email = input("Dime tu email")
        numeros = input("Dime tu munero")
        agenda.append([nombre,apellidos,email,numeros])
        print("Es gurdado 😊")
    #Añado a la agenda
    elif opcion == 2:
        for i,registro  in enumerate(agenda):
            print(i ,registro)
    elif opcion == 3:
        archivo = open("agenda.bin","wb")
        pickle.dump(agenda,archivo)
        archivo.close()
        print("Es gurdado en bases de datos👌")
    else:
        break