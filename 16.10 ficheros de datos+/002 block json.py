archivo = open("blog.txt","r")

lines = archivo.readlines()

for linea in lines:
    print(linea)