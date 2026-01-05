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