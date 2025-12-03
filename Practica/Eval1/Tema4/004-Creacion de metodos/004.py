class Cliente():
    def __init__(self,nombrecompleto,email):
        self.nombrecompleto =  nombrecompleto
        self.email = email
        
    def setNombreCompleto(self, nuevonombre):
        self.nombrecompleto = nuevonombre

    def setEmail(self, nuevoemail):
        self.email = nuevoemail

    def getNombreCompleto(self):
        return self.nombrecompleto
    def getEmail(self):
        return self.email

cliente1 = Cliente("","")

# Asignando valores con setters
cliente1.setNombreCompleto("Juan Pérez")
cliente1.setEmail("juan.perez@example.com")

# Obteniendo valores con getters
print("Nombre del cliente:", cliente1.getNombreCompleto())
print("Email del cliente:", cliente1.getEmail())


