#Crud
#Create 
# Read
# Update
#delete
class Cliente():
    def __init__(self):
        self.emil = None
        self.nombre = None
        self.direccion = None
print("prora,a de gwsriom de clientes vO.1 Bohdan Sydorenko")

print("Seleciona una opcion \n" \
       "\n 1.-Insertae un cliente" \
       "\n 2.-Lista cliemtes " \
       "\n 3.-Actulizar clientes" \
       "\n 4.-Elimunar cliemtes ")



#Creo una licta Vacia
clientes = [] 

while  True : # esto desata en bucle infinito pero controlo
    # Le permito escoger una opcion

    opcion = input("Esgose una opcion")

    #conviarto a enteto
    opcion = int(opcion)

    if opcion == 1:
        print("Vamos a INsertar un cliente")

         # Primero creamos nueve cliente 
        nuevocliente= Cliente()

        #Ahora le propidades 
        nuevocliente.nombre = input("introduce el nomvre del cliente")
        nuevocliente.emil = input("introduse el emiñ de cliente")
        nuevocliente.direccion = input ("introsduce la direccion del cliente")

        # A la lista de clientrs anadimos nuestos cliente cliente 
        clientes.append(nuevocliente) 

    elif opcion == 2:
        print("Vamos a ver los clientes")
        print(clientes)
    elif opcion == 3:
        print("Vamos a actulizar un cliente")
    elif opcion == 4:
        print("Vamos a eliminar un cliente")
    else:
        break