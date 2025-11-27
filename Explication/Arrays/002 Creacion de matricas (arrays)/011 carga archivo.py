import pickle
menu = []

while True:
    print("opciones")
    print("1.Intorduce nueco comida del menu")
    print("2.Listar comidas en el menu")
    print("3. Guardar en archivo")
    print("4.carga la archivo")
    opcion = int(input("Selection una opcion"))
    if opcion == 1:
        comida = input("Introduce el nombre de comida")
        menu.append(comida)
    elif opcion == 2:
        print("Tu comida hasta el momento es")
        for elemnto in menu:
            print(elemnto)
    elif opcion == 3:
        arcrchivo = open("datos.bin","wb")  # Write bimary
        pickle.dump(menu,arcrchivo)
        arcrchivo.close()
        print("Archivo a gurdado")
    elif opcion == 4:
        arcrchivo = open("datos.bin","rb")
        menu = pickle.load(arcrchivo)
        arcrchivo.close()
        print("Archivo a gurdado")
