class Cliente:
    def __init__(self,nombre,apellidos,emails):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = emails


    #metodo set 
    def setApellidos(self,nuevoapellido,nuevonombre,nuevoemail):   
        self.email = nuevoemail
        self.apellidos = nuevoapellido
        self.nombre = nuevonombre
        
    #metodo get 
    def getApellidos(self):
        return self.apellidos
    def getNombre(self):
        return self.nombre
    def getEmail(self):
        return self.email
    #consturtor de parametros 
    def display_info(self):
        print("Nombre de cliente",self.nombre,"Apellido de cliente",self.apellidos,".Email de cliente",self.email)


#crear clases 
cliente1 = Cliente("Ana", "Martínez López", "ana.martinez@example.com")
cliente2 = Cliente("Carlos", "Ruiz Gómez", "carlos.ruiz@example.com")
cliente3 = Cliente("Lucía", "Fernández Torres", "lucia.fernandez@example.com")

#mostar que set get trabajo
print("Nombre de cliente",cliente1.getNombre(),".Apellido de cliente",cliente1.getApellidos(),".Email de cliente",cliente1.getEmail())
print("Nombre de cliente",cliente2.getNombre(),".Apellido de cliente",cliente2.getApellidos(),".Email de cliente",cliente2.getEmail())
print("Nombre de cliente",cliente3.getNombre(),".Apellido de cliente",cliente3.getApellidos(),".Email de cliente",cliente3.getEmail())

#mostar todo los clientes 
cliente1.display_info()
cliente2.display_info()
cliente3.display_info()