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
    def dameDatos(self):
        return self.nombre+" "+self.apellidos   

class Alumno(Persona):
    def __init__(self,nombre,apellidos,email,direccion):
        super().__init__(nombre,apellidos,email,direccion)
    def dameDatos(self):
        return self.nombre+" "+self.apellidos
    
class Persona:
    def __init__(self, nombre, apellidos, email="", direccion=""):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.direccion = direccion
    def dameDatos(self):
        return "Persona"+self.nombre+" "+self.apellidos



class Profesor(Persona):
    def __init__(self, nombre, apellidos):
        super().__init__(nombre, apellidos)

    def dameDatos(self):
        return "Profesor"+self.nombre+" "+self.apellidos


class Alumno(Persona):
    def __init__(self, nombre, apellidos, email, direccion):
        super().__init__(nombre, apellidos, email, direccion)

    def dameDatos(self):
        return "Alumno"+self.nombre+" "+self.apellidos


profesor = Profesor("Juan", "Garcia")
alumno = Alumno("Jose Vicente", "Carratala", "jose.vicente@carratala.com", "Avda. Principal 123")


print(profesor.dameDatos())
print(alumno.dameDatos())