class Cliente():
    def __init__(self,nuevonombre,nuevoemail):
        self.nombre = nuevonombre
        self.email = nuevoemail

clientes = []

clientes.append(Cliente("Jose visente","info@email"))

clientes.append(Cliente("Bohdan","juan.email"))

print(clientes)