# Indroduccion brece y contexalizacion
En nuestra clase sobre Utilización avanzada de clases, hemos estudiado cómo crear jerarquías de clases a través de la herencia y cómo aplicar polimorfismo. Como parte del videojuego que estoy desarrollando, necesito crear diferentes tipos de alumnos para gestionarlos en mi sistema educativo virtual.




# Desarrollo técnico correcto y preciso
## app.py
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
### Crear clases `Profesor` y `Alumno` que es la sub clase de la `Persona`
```
class Profesor(Persona):
    def __init__(self,nombre,apellidos,email,direccion):
        super().__init__(nombre,apellidos,email,direccion)

class Alumno(Persona):
    def __init__(self,nombre,apellidos,email,direccion):
        super().__init__(nombre,apellidos,email,direccion)
```
### Crear clases `AlumnoOnline` y `AlumnoPresencial` que es la sub clase de la `Alumno`
```
class AlumnoOnline(Alumno):
    def __init__(self,nombre,apellidos,email,direccion):
        super().__init__(nombre,apellidos,email,direccion) 

class AlumnoPresencial(Alumno):
    def __init__(self,nombre,apellidos,email,direccion):
        super().__init__(nombre,apellidos,email,direccion) 
```
### inserta en la diferte clase valores 
```
profesor = Profesor("Juan", "Pérez", "juan.perez@correo.com", "Calle Falsa 123")
alumno = Alumno("Ana", "Gómez", "ana.gomez@correo.com", "Calle Real 45")
alumno_online = AlumnoOnline("Luis", "Martínez", "luis.martinez@correo.com", "Avenida Sol 10")
alumno_presencial = AlumnoPresencial("Marta", "López", "marta.lopez@correo.com", "Plaza Mayor 7")
```
### imprimir com la `dameDatos()`
```
print(profesor.dameDatos())          
print(alumno.dameDatos())            
print(alumno_online.dameDatos())     
print(alumno_presencial.dameDatos())
```

# Codigo completa
## app.py
```
class Persona:
    def __init__(self,nombre,apellidos,email,direccion):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.direccion = direccion
    def dameDatos(self):
        return self.nombre+" "+self.apellidos
    
class Profesor(Persona):
    def __init__(self,nombre,apellidos,email,direccion):
        super().__init__(nombre,apellidos,email,direccion)

class Alumno(Persona):
    def __init__(self,nombre,apellidos,email,direccion):
        super().__init__(nombre,apellidos,email,direccion)

class AlumnoOnline(Alumno):
    def __init__(self,nombre,apellidos,email,direccion):
        super().__init__(nombre,apellidos,email,direccion) 

class AlumnoPresencial(Alumno):
    def __init__(self,nombre,apellidos,email,direccion):
        super().__init__(nombre,apellidos,email,direccion)       

profesor = Profesor("Juan", "Pérez", "juan.perez@correo.com", "Calle Falsa 123")
alumno = Alumno("Ana", "Gómez", "ana.gomez@correo.com", "Calle Real 45")
alumno_online = AlumnoOnline("Luis", "Martínez", "luis.martinez@correo.com", "Avenida Sol 10")
alumno_presencial = AlumnoPresencial("Marta", "López", "marta.lopez@correo.com", "Plaza Mayor 7")


print(profesor.dameDatos())          
print(alumno.dameDatos())            
print(alumno_online.dameDatos())     
print(alumno_presencial.dameDatos())
```

# Cierre/Conclusión enlazando con la unidad
Este ejercicio se relaciona directamente con el videojuego educativo en desarrollo, ya que permite gestionar distintos tipos de personajes (profesores, alumnos presenciales y alumnos online) de manera estructurada y flexible.se reutiliza código común, y mediante el polimorfismo el sistema puede tratar a todos los personajes como Persona, facilitando futuras ampliaciones del juego, como añadir nuevos tipos de alumnos o comportamientos específicos sin modificar la estructura base.