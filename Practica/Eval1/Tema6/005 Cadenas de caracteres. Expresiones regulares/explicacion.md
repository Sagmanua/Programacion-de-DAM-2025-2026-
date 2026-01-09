# Indroduccion brece y contexalizacion
En mi tiempo libre disfruto mucho jugando videojuegos y viendo series anime. Estas actividades me ayudan a relajarme y desconectar después de un día largo, además de despertar mi interés por la tecnología y la programación.
En muchos videojuegos y aplicaciones se manejan constantemente textos como nombres de usuario, direcciones o listas de datos. Por eso, el uso de cadenas de caracteres es fundamental en programación, ya que nos permite manipular, validar y transformar información de forma eficiente en proyectos reales.

# Desarrollo técnico correcto y preciso
## app.py
### importe re para hace la patron
```
import re
``` 

### declara varible 
```
nombre = "Jose Vicente"
```
### usa `split` para dividir `nombre`
```
partido = nombre.split()
```
### hago una patron para compravar datos
```
patron = re.compile(
    r'^(Calle|Avenida|Av\.?|Plaza|Pza\.?|Camino)\s+'
    r'[A-Za-zÁÉÍÓÚÜÑáéíóúüñ\s]+?\s+'
    r'\d+\s*,?\s*'
    r'(0[1-9]|[1-4]\d|5[0-2])\d{3}$'
)
```

### creo variables para pronar patron
```
direccion_valida = "Calle Mayor 15, 28013"
direccion_no_valida = "Mayor Calle quince 280"
```
### imprimir resulatado
```
print("Dirección válida:", bool(patron.match(direccion_valida)))
print("Dirección no válida:", bool(patron.match(direccion_no_valida)))
```

### creo una array de numeros
```
datos = "uno,dos,tres,cuatro"
```

### slit array y dentro añado `,` denro de array 
```
lista = datos.split(",")
```
### conjunto array que dentro tiene `,` despues de cada valor u imprimir array
```
cadena_unida = "-".join(lista)

print(cadena_unida)
```

# Codigo completa

```
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

print("Dirección válida:", bool(patron.match(direccion_v alida)))
print("Dirección no válida:", bool(patron.match(direccion_no_valida)))




datos = "uno,dos,tres,cuatro"


lista = datos.split(",")

cadena_unida = "-".join(lista)

print(cadena_unida)

```

# Cierre/Conclusión enlazando con la unidad
El uso de cadenas de caracteres, junto con métodos como split() y join(), y el apoyo de expresiones regulares, es esencial para cualquier proyecto de programación.
Estos conceptos serán muy útiles en el futuro para desarrollar aplicaciones más completas, desde sistemas de registro hasta videojuegos o plataformas relacionadas con mis hobbies, como el seguimiento de series anime o la gestión de perfiles de jugadores. Dominar estas herramientas facilita trabajar con texto de forma clara, segura y eficiente.