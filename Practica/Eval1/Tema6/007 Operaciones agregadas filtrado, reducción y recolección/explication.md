# Indroduccion brece y contexalizacion
¡Hola! Soy un entusiasta del anime y me divierto jugando videojuegos durante mucho tiempo cada día. Hoy te voy a enseñar cómo generar y manipular conjuntos en Python, algo que puede ser muy útil para organizar mis colecciones de juegos o películas favoritas.




# Desarrollo técnico correcto y preciso
## app.py
### import math
```
import random
```

### Genera un conjunto aleatorio: Crea una función  `genera_conjunto` que genere un conjunto de 9 números enteros aleatorios entre 1 y 9.
```
def genera_conjunto():
    conjuntos = set()
    while len(conjuntos) < 9:
        conjuntos.add(random.randint(1, 9))
    return conjuntos
```

#### declara una array con `set`
```
conjuntos = set()
```
#### creao una bucle `while` con 9 cicles para valorar 9 numeros es array y añoado en array
```
while len(conjuntos) < 9:
    conjuntos.add(random.randint(1, 9))
```
#### return `conjuntos` 
```
return conjuntos
```
### llamar funcion `genera_conjunto`
```
print(genera_conjunto())

```

### Comprueba si el conjunto es correcto: Crea una función llamada es_correcto que reciba un conjunto como parámetro y devuelva True si contiene los números del 1 al 9, y False en caso contrario.
```
def es_correcto(conjuntos):
    conjunto_corecta = {1,2,3,4,5,6,7,8,9}
    if conjunto_corecta == conjuntos:
        return True
    else:
        return False
```
#### declara `conjunto_corecta` que numeros esta corectas 
```
conjunto_corecta = {1,2,3,4,5,6,7,8,9}
```

#### compobar si numeros esta correctas or no y return `True` o `False` depende de comprobacion 
```
if conjunto_corecta == conjuntos:
    return True
else:
    return False
```

### llamar funcion `es_correcto`
```
print(es_correcto(genera_conjunto()))
```

### Elimina un número aleatorio: Crea una función llamada elimina_numero que reciba un conjunto y elimine un número aleatorio de él. Devuelve el conjunto modificado.
```
def remove_number(conjuntos):
    numero = random.choice(tuple(conjuntos))
    conjuntos.remove(numero)
    return conjuntos
```
### llamar funcion `es_correcto`
```
print(remove_number(genera_conjunto()))
```


# Codigo completa

```
import random


def genera_conjunto():
    conjuntos = set()
    while len(conjuntos) < 9:
        conjuntos.add(random.randint(1, 9))
    return conjuntos

print(genera_conjunto())

def es_correcto(conjuntos):
    conjunto_corecta = {1,2,3,4,5,6,7,8,9}
    if conjunto_corecta == conjuntos:
        return True
    else:
        return False
    
print(es_correcto(genera_conjunto()))

def remove_number(conjuntos):
    numero = random.choice(tuple(conjuntos))
    conjuntos.remove(numero)
    return conjuntos

print(remove_number(genera_conjunto()))

```

# Cierre/Conclusión enlazando con la unidad
En resumen, este ejercicio consolida el uso de conjuntos (set) para garantizar valores únicos, la modularidad mediante funciones y el control de excepciones para crear programas robustos. Es la base práctica para gestionar datos sin recurrir a estructuras secuenciales.