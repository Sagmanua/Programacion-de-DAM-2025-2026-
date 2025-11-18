menu = []

while True:
    comida = input("Introduce el nombre de comida")
    menu.append(comida)
    print("Tu comida hasta el momento es")
    for elemnto in menu:
        print(elemnto)