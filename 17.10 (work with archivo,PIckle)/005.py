acrchivo = open("basedatos.txt","r")
lineas = acrchivo.readlines()
for linea in lineas:
    print(linea)
acrchivo.close