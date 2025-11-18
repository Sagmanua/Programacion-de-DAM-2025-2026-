menu = []

while True:
    print("opciones")
    print("1.Intorduce nueco comida del menu")
    print("2.Listar comidas en el menu")
    opcion = int(input("Selection una opcion"))
    if opcion == 1:
        comida = input("Introduce el nombre de comida")
        menu.append(comida)
    elif opcion == 2:
        print("Tu comida hasta el momento es")
        for elemnto in menu:
            print(elemnto)