# Indroduccion brece y contexalizacion

En el mundo de los videojuegos y las películas, los objetos y personajes suelen tener características y comportamientos comunes, pero también particularidades propias. Por ejemplo, un juego puede tener diferentes tipos de personajes como héroes, villanos y NPCs, todos con atributos básicos como nombre o vida, pero cada uno con habilidades o acciones específicas.




# Desarrollo técnico correcto y preciso
### Create super class `Persona` y gurdar informacion dentro de este clase 
class Persona:
    def __init__(self,nombre,apellidos,email,direccion):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.direccion = direccion
### dentro de clase `Persona` creo una funcion `dameDatos` que return `nombre` y `apellidos`
```
def dameDatos(self):
    return self.nombre+" "+self.apellidos
```
### Crear clases `Profesor` y  que es la sub clase de la `Persona`
```
class Profesor(Persona):
    def __init__(self,nombre,apellidos,email,direccion):
        super().__init__(nombre,apellidos,email,direccion)
```
### Crear clases `Profesor` y  que es la sub clase de la `Persona` pero añado `email` y `direccion` y configurar la `dameDatos` para 2 valores
```
class Alumno(Persona):
    def __init__(self,nombre,apellidos,email,direccion):
        super().__init__(nombre,apellidos)
        self.email = email
        self.direccion = direccion
    def dameDatos(self):
        return self.nombre+" "+self.apellidos+""+self.email+""+self.direccion
```
### da valor a la clases 
```
profesor = Profesor("Juan", "Garcia")
alumno = Alumno("Jose Vicente", "Carratala", "jose.vicente@carratala.com", "Avda. Principal 123")
```

### imprimir con la `dameDatos`
```
print(profesor.dameDatos())
print(alumno.dameDatos())
```


# Codigo completa
## app.py
```
class Persona:
    def __init__(self,nombre,apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
    def dameDatos(self):
        return self.nombre+" "+self.apellidos
    
class Profesor(Persona):
    def __init__(self,nombre,apellidos):
        super().__init__(nombre,apellidos)
    def dameDatos(self):
        return self.nombre+" "+self.apellidos
 

class Alumno(Persona):
    def __init__(self,nombre,apellidos,email,direccion):
        super().__init__(nombre,apellidos)
        self.email = email
        self.direccion = direccion
    def dameDatos(self):
        return self.nombre+" "+self.apellidos+""+self.email+""+self.direccion

profesor = Profesor("Juan", "Garcia")
alumno = Alumno("Jose Vicente", "Carratala", "jose.vicente@carratala.com", "Avda. Principal 123")


print(profesor.dameDatos())
print(alumno.dameDatos())


```

# Cierre/Conclusión enlazando con la unidad
Este ejercicio demuestra cómo se aplica el polimorfismo en la programación orientada a objetos. Aunque tanto Profesor como Alumno tienen un método llamado dameDatos, cada uno devuelve información diferente según su tipo, mostrando que un mismo método puede comportarse de manera distinta dependiendo del objeto que lo llame.