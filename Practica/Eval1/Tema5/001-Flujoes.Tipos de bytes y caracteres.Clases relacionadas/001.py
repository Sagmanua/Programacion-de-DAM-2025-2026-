nombre = input("Introduce el nombre: ")
email = input("Introduce el email: ")

with open("agenda.txt", "a") as archivo:
    archivo.write(nombre + ", " + email + "\n")


print("Contacto guardado con éxito.")

with open("agenda.txt", "r") as archivo:
    contactos = archivo.readlines()
for contacto in contactos:
    print(contacto.strip())