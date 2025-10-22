class Cliente():
    def __init__(self,nombre,apellidos,email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email

print("----------------")
print("-----------------")

Cliente = []

while True:
    print("escogr una opcion")
    print("1. Inserta un cliene")
    print("2.listar clientes")
    print("3.Actulizarr un cliente")
    print("4.Eliminar un cliente")
    opcion = int(input("Escoge una opcion"))