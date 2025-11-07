class Cliente():
    def __init__(self ):
        self.email = None
        self.nombre = None
        self.direccion = None

clientes = []  

while True: 
    print("Selecciona una opción: ")
    print("1.-Insertar un cliente")
    print("2.-Listar clientes")

    opcion = input("Escoge una opción: ")
    opcion = int(opcion)   
  
    if opcion == 1:
        print("Vamos a insertar un cliente")

        nuevocliente = Cliente()
        nuevocliente.nombre = input("Introduce el nombre del cliente: ")
        nuevocliente.email = input("Introduce el email del cliente: ")
        nuevocliente.direccion = input("Introduce la direccion del cliente: ")
        clientes.append(nuevocliente)
    elif opcion == 2:
        print("Vamos a ver los clientes")
        for cliente in clientes:
            print("Nombre:", cliente.nombre)
            print("Email:", cliente.email)
            print("Dirección:", cliente.direccion)

