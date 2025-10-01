#Crud
#Create 
# Read
# Update
#delete

print("prora,a de gwsriom de clientes vO.1 Bohdan Sydorenko")

print("Seleciona una opcion \n" \
       "1.- Insertae un cliente" \
       "2.-lista cliemtes " \
       "3,- Actulizar clientes" \
       "4.Elimunar cliemtes ")



#Creo una licta Vacia
clientes = [] 

while  True : # esto desata en bucle infinito pero controlo
    # Le permito escoger una opcion

    opcion = input("Esgose una opcion")

    #conviarto a enteto
    opcion = int(opcion)

    if opcion == 1:
        print("Vamos a INsertar un cliente")
        nuevocliente = input("introduce el nomvre del cliente")
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