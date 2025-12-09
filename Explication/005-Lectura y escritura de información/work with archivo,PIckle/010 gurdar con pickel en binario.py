import pickle

class Cliente():
    def __init__(self,nuevonombre,nuevoemail):
        self.nombre = nuevonombre
        self.email = nuevoemail

clientes = []

clientes.append(Cliente("Jose visente","info@email"))

clientes.append(Cliente("Bohdan","juan.email"))

archivo = open("clientes.bin","wb")

pickle.dump(clientes,archivo)
archivo.close