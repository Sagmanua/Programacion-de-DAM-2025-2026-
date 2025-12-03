menu = []

while True:
    print("opciones")
    print("1.Intorduce nueco comida del menu")
    print("2.Listar comidas en el menu")
    opcion = input("Selection una opcion")
    comida = input("Introduce el nombre de comida")
    menu.append(comida)
    print("Tu comida hasta el momento es")
    for elemnto in menu:
        print(elemnto)