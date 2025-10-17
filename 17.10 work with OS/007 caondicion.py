import os

carpeta = input("Indica una carpeta: ")
grande = 1024 * 1024 * 1024  # 1 GB

for directorio, carpetas, archivos in os.walk(carpeta):
    for archivo in archivos:
        ruta = os.path.join(directorio, archivo)
        try:
            if os.path.getsize(ruta) > grande:
                print("------------------")
                print(ruta, os.path.getsize(ruta) / (1024 * 1024), "MB")
        except:
            pass




# C:\Users\BohdanSydorenko\Documents\GitHub ejemplo