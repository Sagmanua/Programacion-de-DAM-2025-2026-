#Declaramos una clase

class Cliente():
    def __init__(self):
        self.emil = None
        self.nombre = None
        self.direccion = None
#usamos la clase instanciando en un objeto
cliente1 = Cliente()
cliente1.emil = "jorse@empresa"
cliente1.nombre = "Jose"
cliente1.direccion = "la calle de Jose"
