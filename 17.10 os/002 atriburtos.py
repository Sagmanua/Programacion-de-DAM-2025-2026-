import os

carpeta = input("indica una carpeta")

elementos = os.listdir(carpeta)

for elemento in elementos:
    ruta = os.path.join(carpeta, elemento)
    print(ruta)
    print(os.path.getsize(ruta)/(1024*1024),"mB")
    print(os.path.getatime(ruta))


# C:\Users\BohdanSydorenko\Documents\GitHub ejemplo