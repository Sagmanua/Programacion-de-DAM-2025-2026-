import json
with open("block.json", "r") as archivo:
    contenido = json.load(archivo)
for articulo in contenido:
    print("####### ARTICULO ########")
    print(f"Título: {articulo['titulo']}")
    print(f"Fecha: {articulo['fecha']}")
    print(f"Autor: {articulo['autor']}")
    print(f"Contenido: {articulo['contenido']}")
    print("#########################")
    print("")