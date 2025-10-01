#Declaramos una clase

class Cliente():
    def __init__(self):
        self.emil = None
        self.nombre = None
        self.direccion = None
#usamos la clase instanciando en un objeto
cliente1 = Cliente()
cliente1.emil = input("Indroduse el emil del cliente")
cliente1.nombre = input("INtroduse el nobmre del cliente")
cliente1.direccion = input("Untroduse la dirreccion del cliente")

print(cliente1)
print(cliente1.emil)
print(cliente1.nombre)
print(cliente1.direccion)
