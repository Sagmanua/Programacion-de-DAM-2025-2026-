import pickle

class Cliente():
    def __init__(self,nombre,apellidos,email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email

print("----------------")
print("-----------------")

try:  #### Ojo que igual no existe el archivo ######
  archivo = open("clientes.bin",'rb')
  clientes = pickle.load(archivo)
  archivo.close
except:
  print("No existe archivo de datos")

clientes = []

while True:
    archivo = open("clientes.bin","wb")
    pickle.dump(clientes,archivo) 
    archivo.close

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
        idificador = 0
        for cliente in clientes:
            print("este es el cliente con id",idificador)
            print(cliente.nombre, cliente.apellidos, cliente.email)
            idificador +=1
        

    elif opcion == 3:
        idificador = int(input("Introduce el id para modificar "))
        nombre  = input("Introduce el nombre")
        apellidos = input("Introduce los appellidos")
        email = input("Introduce el email")
        clientes[idificador].nombre = nombre
        clientes[idificador].apellidos = apellidos
        clientes[idificador].email = email

        

    elif opcion == 4:
        idificador= int(input("Introduce el id para elemianar"))
        confirmacon = (input("Estas ssegura (S/N)")).lower
        if confirmacon == "S" or confirmacon == "s":
            clientes.pop(idificador)
        elif confirmacon == "n" or confirmacon =="N":
            print("Canselado")
        else:
            print("Opcion no valida")
                