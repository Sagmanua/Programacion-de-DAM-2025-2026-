import json
with open("block.json", "r") as archivo:
    contactos = archivo.readlines()
for articulo in contactos:
    print("####### ARTICULO ########")
    print(f"Título: {articulo['titulo']}")
    print(f"Fecha: {articulo['fecha']}")
    print(f"Autor: {articulo['autor']}")
    print(f"Contenido: {articulo['contenido']}")
    print("#########################")
    print("")