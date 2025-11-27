archivo = open("clientes.csv","r")

lineas = archivo.readlines()
conjunto_datos = []

for linea in lineas:
    pardido = linea.split(".")
    conjunto_datos.append(pardido)
print(conjunto_datos)