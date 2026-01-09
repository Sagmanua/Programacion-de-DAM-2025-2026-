import re

nombre = "Jose Vicente"

partido = nombre.split()

print(partido)

patron = re.compile(
    r'^(Calle|Avenida|Av\.?|Plaza|Pza\.?|Camino)\s+'
    r'[A-Za-zÁÉÍÓÚÜÑáéíóúüñ\s]+?\s+'
    r'\d+\s*,?\s*'
    r'(0[1-9]|[1-4]\d|5[0-2])\d{3}$'
)

direccion_valida = "Calle Mayor 15, 28013"
direccion_no_valida = "Mayor Calle quince 280"

print("Dirección válida:", bool(patron.match(direccion_valida)))
print("Dirección no válida:", bool(patron.match(direccion_no_valida)))




datos = "uno,dos,tres,cuatro"


lista = datos.split(",")

cadena_unida = "-".join(lista)

print(cadena_unida)
