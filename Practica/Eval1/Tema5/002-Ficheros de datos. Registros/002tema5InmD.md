# Indroduccion brece y contexalizacion





# Desarrollo técnico correcto y preciso
## Al primero creeo una json file con nombre `bñock.json` y gurdo informcionen ella 
```
[
  {
    "titulo": "Primer artículo",
    "fecha": "2025-10-16",
    "autor": "Jose Vicente Carratalá",
    "contenido": "Este es el contenido del primer artículo"
  },
  {
    "titulo": "Segundo artículo",
    "fecha": "2025-10-17",
    "autor": "Jose Vicente Carratalá",
    "contenido": "Este es el contenido del segundo artículo"
  }
]
```

# Codigo completa
## Python
```
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
```
## JSON
```
[
  {
    "titulo": "Primer artículo",
    "fecha": "2025-10-16",
    "autor": "Jose Vicente Carratalá",
    "contenido": "Este es el contenido del primer artículo"
  },
  {
    "titulo": "Segundo artículo",
    "fecha": "2025-10-17",
    "autor": "Jose Vicente Carratalá",
    "contenido": "Este es el contenido del segundo artículo"
  }
]
```

# Cierre/Conclusión enlazando con la unidad
