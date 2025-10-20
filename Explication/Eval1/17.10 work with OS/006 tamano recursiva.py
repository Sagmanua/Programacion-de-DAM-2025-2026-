import os
suma = 0

carpeta = input("Indica una carpeta")

for directorio, carpetas, archivos in os.walk(carpeta):
    for archivo in archivos:
        ruta = os.path.join(directorio, archivo)
        try:
            suma += os.path.getsize(ruta)
        except:
            pass

print("la carpeta ocup:")
print(suma/(1024*1024),"MB")

# C:\Users\BohdanSydorenko\Documents\GitHub ejemplo