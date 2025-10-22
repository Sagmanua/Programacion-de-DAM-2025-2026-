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
        email = input("Introduce el email")
        clientes.append(Cliente(nombre,apellidos,email))


        
    elif opcion == 2:
        print(Cliente.nombre,Cliente.apellidos,Cliente.email)
        

    elif opcion == 3:
        idificador = input("Introduce el id para modificar ")
        nombre  = input("Introduce el nombre")
        apellidos = input("Introduce los appellidos")
        email = input("Introduce el email")
        clientes[idificador].nombre = nombre
        clientes[idificador].apellidos = apellidos
        clientes[idificador].email = email

        

    elif opcion == 4:
        print()