# Indroduccion brece y contexalizacion
En nuestro mundo digital, muchas personas usan series anime y películas como fuente de inspiración para crear apps personales (listas de favoritos, calendarios de visionado, contactos de comunidad, etc.). Este ejercicio muestra cómo dar el primer paso técnico: manejar información simple (nombre + email) guardándola en un archivo de texto (agenda.txt) y recuperándola después. Aprenderás lectura y escritura en archivos —una habilidad básica y reutilizable cuando construyas una agenda o gestor de favoritos inspirado en tus series preferidas.




# Desarrollo técnico correcto y preciso
## Python
### Creo acrhivo  `agenda.txt` para guardar informcacion (con manos sin codigo)
### Inputs para usario puede introduce su informacion
```
nombre = input("Introduce el nombre: ")
email = input("Introduce el email: ")
```
### Gurdo informcaion que introduce usario en el acrhivo  `agenda.txt`
```
with open("agenda.txt", "a") as archivo:
    archivo.write(nombre + ", " + email + "\n")
```
### Ahora leido informcaion de acrhivo  `agenda.txt` para muestro informacion de usario
```
with open("agenda.txt", "r") as archivo:
    contactos = archivo.readlines()
```
### Ahora muestro informcaion de usario en consola
```
for contacto in contactos:
    print(contacto.strip())
```
# Codigo completa
## Python
```
nombre = input("Introduce el nombre: ")
email = input("Introduce el email: ")

with open("agenda.txt", "a") as archivo:
    archivo.write(nombre + ", " + email + "\n")

print("Contacto guardado con éxito.")

with open("agenda.txt", "r") as archivo:
    contactos = archivo.readlines()
for contacto in contactos:
    print(contacto.strip())
```

# Cierre/Conclusión enlazando con la unidad
Este ejercicio pone en práctica los conceptos de lectura y escritura de archivos en Python, mostrando cómo guardar y recuperar información de manera sencilla. Gracias a esto entendemos cómo los programas pueden mantener datos de forma permanente, lo cual es fundamental para crear aplicaciones útiles, como una agenda personal o un organizador de series anime y películas. Así, se conecta la teoría de la unidad con una aplicación real y motivadora.