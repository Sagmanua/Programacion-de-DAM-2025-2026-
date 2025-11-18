import os

carpeta = input("Indica una carpeta")

for directorio,carpeta,arhivo in os.walk(carpeta):
    print(directorio)
    print(carpeta)
    print(arhivo)
