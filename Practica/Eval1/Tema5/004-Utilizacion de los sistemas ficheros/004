import os

carpeta = input("Ingresa la ruta de la carpeta: ")

if os.path.isdir(carpeta):
    elementos = os.listdir(carpeta)
    print("\nContenido de la carpeta:\n")
    for elemento in elementos:
        ruta_completa = os.path.join(carpeta, elemento)
        print(ruta_completa)



carpeta = input("Ingresa la ruta de la carpeta: ")

if os.path.isdir(carpeta):
    print("\nRecorriendo la carpeta y sus subcarpetas:\n")
    for ruta_actual, carpetas, archivos in os.walk(carpeta):
        print(f"Carpeta actual: {ruta_actual}")
        for nombre in archivos:
            ruta_completa = os.path.join(ruta_actual, nombre)
            print(f"  Archivo: ",ruta_completa)

    archivo = input("Ingresa la ruta del archivo de texto: ")
    palabra = input("Ingresa la palabra a buscar: ")

with open(archivo, "r", encoding="utf-8") as f:
    print("\nResultado de la búsqueda:\n")
    for numero_linea, linea in enumerate(f, start=1):
        if palabra in linea:
            print(f"Línea {numero_linea}: {linea.strip()}")

