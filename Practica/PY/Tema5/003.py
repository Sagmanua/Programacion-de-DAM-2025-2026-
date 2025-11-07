nombre_archivo = "videojuegos.txt"

with open(nombre_archivo, "w") as archivo:
    archivo.write("MiUsuario123\n")   # <-- Aquí puedes poner tu propio nombre de usuario

with open(nombre_archivo, "a") as archivo:
    archivo.write("The Legend of Zelda\n\n")
    archivo.write("Minecraft\n\n")
    archivo.write("Super Mario Odyssey\n\n")
    archivo.write("Halo Infinite\n\n")  # Puedes añadir más si quieres

with open(nombre_archivo, "r") as archivo:
    contenido = archivo.read()
    print(contenido)
