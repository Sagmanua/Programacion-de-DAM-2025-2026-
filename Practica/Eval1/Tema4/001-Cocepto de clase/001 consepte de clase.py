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
