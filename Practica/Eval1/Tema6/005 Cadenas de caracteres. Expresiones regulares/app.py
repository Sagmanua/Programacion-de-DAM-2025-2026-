import re

#Parte 1
nombre = "Bohdan Sydorenko"

partido = nombre.split()

print(partido)

#Parte 2
patron = re.compile(
    r'^(Calle|Avenida|Av\.?|Plaza|Pza\.?|Camino)\s+'
    r'[A-Za-zÁÉÍÓÚÜÑáéíóúüñ\s]+?\s+'
    r'\d+\s*,?\s*'
    r'(0[1-9]|[1-4]\d|5[0-2])\d{3}$'
)

# Direcciones de prueba
direccion_valida = "Calle Mayor 15, 28013"
direccion_no_valida = "Mayor Calle quince 280"

print("Dirección válida:", bool(patron.match(direccion_valida)))
print("Dirección no válida:", bool(patron.match(direccion_no_valida)))

#Parte 3 

# Cadena original
datos = "uno,dos,tres,cuatro"

# Convertir cadena en lista
lista = datos.split(",")

# Unir la lista en una nueva cadena
cadena_unida = "-".join(lista)

# Imprimir resultado
print(cadena_unida)
