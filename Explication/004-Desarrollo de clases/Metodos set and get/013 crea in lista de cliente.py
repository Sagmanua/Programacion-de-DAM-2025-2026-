class Cliente():
    def __init__(self):
        self.nonmbreCompleto = None
        self.email = None
    def setNomreCompleto(self,nuvonombre):
        self.nonmbreCompleto = nuvonombre
    def setEmail(self,nueboemail):
        self.email = nueboemail
    def getNOmbreCopmlrto(self):
        return self.nonmbreCompleto
    def getEmail(self):
        return self.email
    
clientes = [] ##################Meto una lista de cliente vacia
while True:
    print("" \
    "gestoe de clientes v0.1 Bohdan Sydorenko" \
    "Seleciona una opcion" \
    "1.-Insertar ub nuevo cliente" \
    "2.-obtener lisradi de cliente")
    opcion= int(input("indica tu opcion"))

    if opcion == 1:
        print("vaoy a insertae un cliente") #todo el dato
        nuevocliente = Cliente() # Uso el metodo set para meter ek daro en el objeto 
        nombrecliente = input("introduse tu nombre") 
        nuevocliente.setNomreCompleto(nombrecliente) # Uso el metodo set para el dato en el objeto

        emailcliente = input("emal") #Todo el dato  
        nuevocliente.setEmail(emailcliente)# Uso el metodo set para el dato en el objeto
        clientes.append(nuevocliente)
    elif opcion ==2:
        print("SAco el lsdtado de cliente")
        for cliente in clientes:
            print("nombre", cliente.getNOmbreCopmlrto())
            print("email",cliente.getEmail())
