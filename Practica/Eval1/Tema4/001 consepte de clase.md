```
'''
    001 concepte de clase 
    (c)Bohdan Sydorenk
    Anteriormente hemos visto cómo las clases permiten encapsular código y reutilizarlo. 
    Las clases llevan esta metodología mucho más allá, ya que nos permiten crear objetos que representan entidades del mundo real.
    Para este ejercicio, vamos a crear una clase Cliente que tenga propiedades para almacenar la información de un cliente. 
    Esto nos ayudará a entender cómo encapsular datos dentro de una clase y cómo acceder a ellos mediante métodos.
'''
'''
Que hago:
1.crear una clase
2.obejetos de clientes
3.Imprimir todo
'''
# Definición de la clase Cliente
class Clientes:

    def __init__ (self,email,direeccion,nombre,apellidos):
        self.email =email 
        self.direccion = direeccion
        self.nombre = nombre
        self.apellidos = apellidos

# Creación de objetos de la clase Cliente
cliente1 = Clientes("info@gmail.com","calle no se ","Pyton","Pytonnest")
cliente2 = Clientes("info@mail.com","calle no se ","Java","Javaest")

#Imprimir 

#----------------Cliente 1 ------------
print("Cliente 1:")
print("Nombre:", cliente1.nombre)
print("Apellidos:", cliente1.apellidos)
print("Email:", cliente1.email)
print("Dirección:", cliente1.direccion)

#----------------Cliente 2 ------------
print("\nCliente 2:")
print("Nombre:", cliente2.nombre)
print("Apellidos:", cliente2.apellidos)
print("Email:", cliente2.email)
print("Dirección:", cliente2.direccion)
```

## 1.-Indroduccion brece y contexalizacion

Para este ejercicio, vamos a trabar con concptos clases y objetos de la Programación Orientada a Objetos (POO) y  crear una clase Cliente que tenga propiedades para almacenar la información de un cliente. Esto nos ayudará a entender cómo encapsular datos dentro de una clase y cómo acceder a ellos mediante método




## 2.-Desarrollo técnico correcto y preciso


1.Voy a crear classe con Clientes con `__init__` para inicializar unos clientes 
```
class Clientes:

    def __init__ (self,email,direeccion,nombre,apellidos):
        self.email =email 
        self.direccion = direeccion
        self.nombre = nombre
        self.apellidos = apellidos
```

2.Instanciar objetos de la clase Client.Asigna valores a las propiedades de cada objeto
```
cliente1 = Clientes("info@gmail.com","calle no se ","Pyton","Pytonnest")
cliente2 = Clientes("info@mail.com","calle no se ","Java","Javaest")
       
```
3.Imprimir todos los clientes 
```
#----------------Cliente 1 ------------
print("Cliente 1:")
print("Nombre:", cliente1.nombre)
print("Apellidos:", cliente1.apellidos)
print("Email:", cliente1.email)
print("Dirección:", cliente1.direccion)

#----------------Cliente 2 ------------
print("\nCliente 2:")
print("Nombre:", cliente2.nombre)
print("Apellidos:", cliente2.apellidos)
print("Email:", cliente2.email)
print("Dirección:", cliente2.direccion)
```


## 3.-Aplicacion practica

```
# Definición de la clase Cliente
class Clientes:

    def __init__ (self,email,direeccion,nombre,apellidos):
        self.email =email 
        self.direccion = direeccion
        self.nombre = nombre
        self.apellidos = apellidos

# Creación de objetos de la clase Cliente
cliente1 = Clientes("info@gmail.com","calle no se ","Pyton","Pytonnest")
cliente2 = Clientes("info@mail.com","calle no se ","Java","Javaest")

#Imprimir 

#----------------Cliente 1 ------------
print("Cliente 1:")
print("Nombre:", cliente1.nombre)
print("Apellidos:", cliente1.apellidos)
print("Email:", cliente1.email)
print("Dirección:", cliente1.direccion)

#----------------Cliente 2 ------------
print("\nCliente 2:")
print("Nombre:", cliente2.nombre)
print("Apellidos:", cliente2.apellidos)
print("Email:", cliente2.email)
print("Dirección:", cliente2.direccion)
```

## 4.-Cierre/Conclusión enlazando con la unidad

En este ejecicio relaxiona con los conceptos de clases,objetos y encapsulación vistos en clase, ya que nos permitió aplicar la teoría de la Programación Orientada a Objetos.En mundo real tienes situaciones donde nesisito gurdar diferente datos y en este caso puedos usamos Clase con init dentro 