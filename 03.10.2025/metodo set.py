class Gato():
    def __init__(self): # Este es una propiedad
        self.color = None 
    def mulla(self): #Este es un metodo (es una accion)
         return "miau"
    def setColor(self,nuevocolor):
        #Por ejemplo aqui podria calidar se eke cikie es un color validos para un gato
        self.color = nuevocolor
gato1 = Gato()
gato1.color = "naranja"  # Aqui sekemos una propiedad diracramente ni es bueba practica
print(gato1.mulla()) # Aqui llammos a un metodo

gato1.setColor("naranja")
