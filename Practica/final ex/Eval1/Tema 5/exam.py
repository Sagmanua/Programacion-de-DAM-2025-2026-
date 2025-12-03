'''
    Exam de final tema 5 mini-Crud con pickle
    (c) Bohdan Sydorenko
'''
'''
Que hago
1.import 
2.class
3.abrir acrcivo bin 
4.bucle infinito
5.crear
6.leer
7.salir
'''

import pickle

class Cliente():
        def __init__(self,nombre,apellidos,email):
            self.nombre = nombre
            self.apellidos = apellidos
            self.email = email
clientes = []

print("mini Crud")
archivo = open("clientes.bin",'rb')
clientes = pickle.load(archivo)
archivo.close()

while True:
    archivo=open("clientes.bin",'wb')
    pickle.dump(clientes,archivo)
    archivo.close()

    print("Escoge una opción:")
    print("1.-Insertar un cliente")
    print("2.-Listar clientes")
    print("3.-Salir de programa")
    opcion = int(input("Escoge una opcion:"))
    
    if opcion == 1:
        nombre = input("Introduce el nombre: ")
        apellidos = input("Introduce la apellido: ")
        email = input("Introduce el email: ")
        clientes.append(Cliente(nombre,apellidos,email))
    elif opcion == 2:
        id = 0
        for cliente in clientes:
            print("id de cliente:",id,cliente.nombre,cliente.apellidos,cliente.email)
            id += 1
    elif opcion == 3:
        break