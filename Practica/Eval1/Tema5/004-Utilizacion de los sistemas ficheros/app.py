import os

# Parte 1
carpeta = input("Indica una carpeta: ")

elementos = os.listdir(carpeta)

for elemento in elementos:
    ruta = os.path.join(carpeta, elemento)
    print(ruta)

# Parte 2
carpeta = input("Indica una carpeta: ")

for directorio,carpetas,archivo in os.walk(carpeta):
    print(directorio)
    print(carpetas)
    print(archivo)

# Parte 3 
archivo = open("mapa.txt",'r') # READ
busca = input("Introduce el término a buscar: ")

lineas = archivo.readlines()

for linea in lineas:
    if busca in linea:
        print("###########################")
        print("Encontrado!: ",linea)   