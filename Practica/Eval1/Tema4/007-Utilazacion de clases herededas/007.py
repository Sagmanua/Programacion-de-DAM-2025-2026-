class Animal:
    def __init__(self, edad, nombre, raza):
        self.edad = edad
        self.nombre = nombre
        self.raza = raza

class Gato(Animal):
    def __init__(self, edad, nombre, raza):
        super().__init__(edad, nombre, raza)

class Perro(Animal):
    def __init__(self, edad, nombre, raza):
        super().__init__(edad, nombre, raza)
gato = Gato(2,"Michi","Siames")
perro = Perro(4,"Rex","Pastor Alemán")

print("Nombre",gato.nombre)
print("Edad",gato.edad)
print("Raza",gato.raza)

print("Nombre",perro.nombre)
print("Edad",perro.edad)
print("Raza",perro.raza)
