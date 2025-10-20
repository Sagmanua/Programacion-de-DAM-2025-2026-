class Cliente():
    def __init__(self):
        self.nombre = None
        self.edad = None
        self.telefonos = ['543809','789123']

#ahora instancio un nuevo
cliente1 = Cliente()

#Ahora le ecribo una propiedad

cliente1.nombre = "Jose Visente "

print("el nombre del cliente es ", cliente1.nombre)

cliente1.telefonos.append('123809')
cliente1.telefonos.append('234798')

print(cliente1.telefonos)