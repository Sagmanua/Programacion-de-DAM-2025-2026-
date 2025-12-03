

## 1.-Indroduccion brece y contexalizacion

En este programa final del examen voy a practicar la creación de clases que incluyan los métodos especiales `__init__`, get y set. Cada clase puede tener su propia información o datos, los cuales representan las características de los objetos que se crean a partir de ella.

En este caso, la clase está diseñada para gestionar y almacenar información de clientes, como su nombre, apellidos y correo electrónico. Los métodos `get` y `set` se utilizan para acceder y modificar los atributos de manera controlada, aplicando el principio de encapsulación, que es fundamental en la programación orientada a objetos.



## 2.-Desarrollo técnico correcto y preciso

### Crea una clase es le basico que hacer 
```
class Cliente:
    pass
```
### Crear proioedades para puedo gurdar inforamcion en clientes 
```
def __init__(self,nombre,apellidos,emails):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = emails
       
```
### Set estos métodos modifican los valores de los atributos.

```
def setApellidos(self,nuevoapellido,nuevonombre,nuevoemail):   
        self.email = nuevoemail
        self.apellidos = nuevoapellido
        self.nombre = nuevonombre
```
### get estos métodos devuelven el valor de un atributo del objeto.

```
def getApellidos(self):
        return self.apellidos
    def getNombre(self):
        return self.nombre
    def getEmail(self):
        return self.email
```
### este metodo para visualice los datos del cliente en un formato legible. 
``` 
def display_info(self):
        print("Nombre de cliente",self.nombre,"Apellido de cliente",self.apellidos,".Email de cliente",self.email)

```
### voy a crear 3 instacias de la clase Cliente este es informacion que guarda 
```
cliente1 = Cliente("Ana", "Martínez López", "ana.martinez@example.com")
cliente2 = Cliente("Carlos", "Ruiz Gómez", "carlos.ruiz@example.com")
cliente3 = Cliente("Lucía", "Fernández Torres", "lucia.fernandez@example.com")  
```

### imprimir al primero imprimir con set y get 
```
print("Nombre de cliente",cliente1.getNombre(),".Apellido de cliente",cliente1.getApellidos(),".Email de cliente",cliente1.getEmail())
print("Nombre de cliente",cliente2.getNombre(),".Apellido de cliente",cliente2.getApellidos(),".Email de cliente",cliente2.getEmail())
print("Nombre de cliente",cliente3.getNombre(),".Apellido de cliente",cliente3.getApellidos(),".Email de cliente",cliente3.getEmail())
```
### imprimir com metodo display_info
```
cliente1.display_info()
cliente2.display_info()
cliente3.display_info()
```

## Codigo completa 

```
'''
    Exam tema 4 mostara classs set get 
    (c) Bohda Sydorenko

'''
'''
Que hace 
1.-Crea una clase 
2.-propiedades 
3.-Set
4.-Get
5.-constructor con parametros
6.-crea tres instancias de la clase
7.-Imprimir todo 
'''
class Cliente:
    def __init__(self,nombre,apellidos,emails):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = emails


    #metodo set 
    def setApellidos(self,nuevoapellido,nuevonombre,nuevoemail):   
        self.email = nuevoemail
        self.apellidos = nuevoapellido
        self.nombre = nuevonombre
        
    #metodo get 
    def getApellidos(self):
        return self.apellidos
    def getNombre(self):
        return self.nombre
    def getEmail(self):
        return self.email
    #consturtor de parametros 
    def display_info(self):
        print("Nombre de cliente",self.nombre,"Apellido de cliente",self.apellidos,".Email de cliente",self.email)


#crear clases 
cliente1 = Cliente("Ana", "Martínez López", "ana.martinez@example.com")
cliente2 = Cliente("Carlos", "Ruiz Gómez", "carlos.ruiz@example.com")
cliente3 = Cliente("Lucía", "Fernández Torres", "lucia.fernandez@example.com")

#mostar que set get trabajo
print("Nombre de cliente",cliente1.getNombre(),".Apellido de cliente",cliente1.getApellidos(),".Email de cliente",cliente1.getEmail())
print("Nombre de cliente",cliente2.getNombre(),".Apellido de cliente",cliente2.getApellidos(),".Email de cliente",cliente2.getEmail())
print("Nombre de cliente",cliente3.getNombre(),".Apellido de cliente",cliente3.getApellidos(),".Email de cliente",cliente3.getEmail())

#mostar todo los clientes 
cliente1.display_info()
cliente2.display_info()
cliente3.display_info()
```

## 4.-Cierre/Conclusión enlazando con la unidad

Con este ejercicio he podido aplicar los conceptos fundamentales de la Programación Orientada a Objetos, especialmente el uso de clases, atributos y métodos. Al crear la clase Cliente y utilizar los métodos `__init__`, `get` y `set`, comprendí cómo se pueden estructurar y proteger los datos dentro de un programa, favoreciendo una mejor organización del código y un acceso controlado a la información.
