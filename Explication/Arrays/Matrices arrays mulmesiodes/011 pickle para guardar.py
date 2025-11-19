import pickle
agenda = []

while True:
    nombre = input("Dime tu nombre")
    apellidos = input("Dime tu apellidos")
    email = input("Dime tu email")
    numeros = input("Dime tu munero")
    #Añado a la agenda
    agenda.append([nombre,apellidos,email,numeros])
    print(agenda)
    archivo = open("agenda.bin","wb")
    pickle.dump(agenda,archivo)
    archivo.close()
