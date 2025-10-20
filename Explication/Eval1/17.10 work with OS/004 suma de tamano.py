import os

suma = 0

carpeta = input("indica una carpeta")

elementos = os.listdir(carpeta)



for elemento in elementos:
    ruta = os.path.join(carpeta, elemento)
    suma += os.path.getsize(ruta)

print("la carpeta ocup:")
print(suma/(1024*1024),"MB")

# C:\Users\BohdanSydorenko\Documents\GitHub ejemplo