class Animal():
    def __init(self):
        self.edad = 0
        self.nombre = ""
        self.raza = ""

class Gato():
    def __init__(self):
        super().__init__()  #ME tralgo todo lo que tenfa la clase superio

class Perro():
    def __init__(self): #ME tralgo todo lo que tenfa la clase superio
        super().__init__()

gato1 = Gato()
print(gato1.edad)

perro1 = Perro
print(perro1.edad)
