import os

carpeta = input("Indica una carpeta: ")
grande = 1024 * 1024 * 1024  # 1 GB

mapa = open("mapa.txt", "a")  # o "w" para sobrescribir cada vez

for directorio, carpetas, archivos in os.walk(carpeta):
    for archivo in archivos:
        ruta = os.path.join(directorio, archivo)
        mapa.write(ruta + "\n")  # agregar salto de línea

mapa.close()  # llamar correctamente a close
print("-----------")


# C:\Users\BohdanSydorenko\Documents\GitHub ejemplo