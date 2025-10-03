class Gato():
    def __init__(self): # Este es una propiedad
        self.color = None 
    def mulla(self): #Este es un metodo (es una accion)
         return "miau"
gato1 = Gato()
gato1.color = "naranja"  # Aqui sekemos una propiedad
print(gato1.mulla()) # Aqui llammos a un metodo