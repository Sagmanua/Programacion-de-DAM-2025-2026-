# Indroduccion brece y contexalizacion
En mis tiempos libres disfruto de los videojuegos y las series anime, donde muchas veces aparecen animales con características únicas o incluso poderes especiales. Inspirándome en eso, quiero crear un pequeño programa que permita administrar información sobre diferentes animales, de una forma similar a como en un videojuego se gestionan los personajes o criaturas.

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
###  Creo la instancia de la clase `Gato` y `Perro`
```
gato = Gato(2,"Michi","Siames")
perro = Perro(4,"Rex","Pastor Alemán")
```
### Muestro todo informacio de clases con print `print`
```
print("Nombre",gato.nombre)
print("Edad",gato.edad)
print("Raza",gato.raza)

print("Nombre",perro.nombre)
print("Edad",perro.edad)
print("Raza",perro.raza)
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
En la vida real (y en el desarrollo de videojuegos o aplicaciones inspiradas en anime o zoología), este tipo de estructuras permite manejar fácilmente diferentes tipos de entidades que comparten características comunes. Por ejemplo, podríamos usarlo para crear una base de datos de mascotas, personajes o criaturas con atributos compartidos y comportamientos específicos según su tipo.