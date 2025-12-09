import json

archivo = open("block.json","r")

contenodido = json.load(archivo)

for linea in contenodido:
    print(linea['Titulo'])
    print(linea['fecha'])
    print(linea['autor'])
    print(linea['contiendo'])