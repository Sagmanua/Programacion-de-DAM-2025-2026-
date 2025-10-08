while True:
    print("dime la que quires hacer:")
    print("1.- INtrodice un nuevo contacto")
    print("2.- Lear todos los contactrs")
    opcion = input("elige opcion")
    opcion = int(opcion)
    if opcion == 1:
        nombre = input("")
        email = input("")
        archivo = open("agenda.txt",'a')
        archivo.write(nombre+","+email+"\n")
        archivo.close()
    elif opcion == 2: 
        archivo =open("agenda.txt",'r')
        lineas = archivo.readlines()
        for linea in lineas:
            print(linea)
        archivo.close()
    
