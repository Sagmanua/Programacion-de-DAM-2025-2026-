cliente1_emil = "info@jocaras.com"
cliente1_dirreccion = " la calle de Jose Visicente "
cliente1_nombre = " Jose Visecente "
cliente1_apellidos = "Carreatalla Sanchis  "

cliente2_emil = "info@jocaras2.com"
cliente2_dirreccion = " la calle de Jose Visicente"
cliente2_nombre = " Jose"
cliente2_apellidos = "Carreatalla"


#Muchos mejor usi de clases 

class Cliente:
    def __init__(self):
        self.email = ""
        self.dirreccion = ""
        self.nombre= ""
        self.apellidos=""
cliente1 = Cliente()
cliente1.email = "info@jocaras.com"
cliente1.dirreccion = " la calle de Jose Visicente "
cliente1.nombre = " Jose Visecente "
cliente1.apellidos = "Carreatalla Sanchis  "

cliente2 = Cliente()

cliente2.email = "info@jocaras2.com"
cliente2.dirreccion = " la calle de Jose Visicente"
cliente2.nombre = " Jose"
cliente2.apellidos = "Carreatalla"