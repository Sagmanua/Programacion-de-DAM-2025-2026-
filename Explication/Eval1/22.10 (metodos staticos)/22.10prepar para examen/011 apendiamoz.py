class Cliente():
    def __init__(self,nombre,apellidos,email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email

print("----------------")
print("-----------------")

clientes = []

while True:
    print("escogr una opcion")
    print("1. Inserta un cliene")
    print("2.listar clientes")
    print("3.Actulizarr un cliente")
    print("4.Eliminar un cliente")
    opcion = int(input("Escoge una opcion"))

    if opcion == 1:
        nombre  = input("Introduce el nombre")
        apellidos = input("Introduce los appellidos")
        emil = input("Introduce el email")
        clientes.apppend(Cliente(nombre,apellidos,email))


        print()
    elif opcion == 2:
        print()

    elif opcion == 3:
        print()

    elif opcion == 4:
        print()