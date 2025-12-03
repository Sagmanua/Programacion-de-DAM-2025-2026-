# Indroduccion brece y contexalizacion
Como aficionado a las series anime y videojuegos, es importante organizar la información de los clientes de una tienda que ofrece estos productos. Para ello, podemos usar clases en programación, que nos permiten agrupar atributos y métodos relacionados con los clientes de manera organizada y segura. Esto facilita el manejo de datos como el nombre completo y el email de cada cliente, garantizando que se acceda a ellos solo mediante métodos controlados (setters y getters).




# Desarrollo técnico correcto y preciso
## Python
### Crea una clase es le basico que hacer 
```
class Cliente:
    pass
```
### Crear proioedades para puedo gurdar inforamcion en clientes 
```
def __init__(self,nombrecompleto,email):
        self.nombrecompleto =  nombrecompleto
        self.email = email
       
```
### Set estos métodos modifican los valores de los atributos.

```
def setNombreCompleto(self, nuevonombre):
    self.nombrecompleto = nuevonombre
def setEmail(self, nuevoemail):
    self.email = nuevoemail

```
### get estos métodos devuelven el valor de un atributo del objeto.

```
def getNombreCompleto(self):
    return self.nombrecompleto
def getEmail(self):
    return self.email
```

### voy a crear 3 instacias de la clase Cliente este es informacion que guarda 
```
cliente1.setNombreCompleto("Juan Pérez")
cliente1.setEmail("juan.perez@example.com")

print("Nombre del cliente:", cliente1.getNombreCompleto())
print("Email del cliente:", cliente1.getEmail())
```

# Codigo completa

```
class Cliente():
    def __init__(self,nombrecompleto,email):
        self.nombrecompleto =  nombrecompleto
        self.email = email
        
    def setNombreCompleto(self, nuevonombre):
        self.nombrecompleto = nuevonombre

    def setEmail(self, nuevoemail):
        self.email = nuevoemail

    def getNombreCompleto(self):
        return self.nombrecompleto
    def getEmail(self):
        return self.email

cliente1 = Cliente("","")

# Asignando valores con setters
cliente1.setNombreCompleto("Juan Pérez")
cliente1.setEmail("juan.perez@example.com")

# Obteniendo valores con getters
print("Nombre del cliente:", cliente1.getNombreCompleto())
print("Email del cliente:", cliente1.getEmail())
```

# Cierre/Conclusión enlazando con la unidad
En esta actividad, hemos aprendido a crear una clase Cliente con atributos privados y métodos setter y getter. Esto nos permite controlar el acceso a los datos y mantener la integridad de la información de los clientes. Esta práctica se relaciona directamente con la unidad de clases y objetos, mostrando cómo encapsular datos y cómo interactuar con ellos mediante métodos específicos, que es un concepto clave en la programación orientada a objetos.