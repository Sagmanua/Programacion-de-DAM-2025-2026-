# Indroduccion brece y contexalizacion





# Desarrollo técnico correcto y preciso
## Python
### Crear super clase `Animal` es clase que clases anterio va a refirir
```
class Animal:
    def __init__(self, edad, nombre, raza):
        self.edad = edad
        self.nombre = nombre
        self.raza = raza
```
### Crear bajo la clase `Gato` y `Perro` en que tiene referencia a super clase `Animal`
```
class Gato(Animal):
    def __init__(self, edad, nombre, raza):
        super().__init__(edad, nombre, raza)

class Perro(Animal):
    def __init__(self, edad, nombre, raza):
        super().__init__(edad, nombre, raza)
```
###  Creo la instancia de la clase Series
```
```
# Codigo completa

```
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

```

# Cierre/Conclusión enlazando con la unidad
