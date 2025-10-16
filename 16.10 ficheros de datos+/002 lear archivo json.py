import json

archivo = open("block.json","r")

contenodido = json.load(archivo)

print(contenodido)