archivo = open("clientes.csv","r")

lineas = archivo.readlines()

for linea in lineas:
    pardido = linea.split(".")
    print(pardido)