# Indroduccion brece y contexalizacion
En nuestro proyecto actual sobre estructuras de almacenamiento, hemos trabajado con listas y cómo manejar diferentes tipos de datos dentro de ellas. Hoy, nos enfocaremos en cómo tratar errores al trabajar con listas que contienen elementos de diferentes tipos, como números y cadenas.

Para mantenernos motivados y relajados mientras programamos, me gusta ver series de anime o películas durante mis descansos. También disfruto jugando videojuegos durante el 70% de mi tiempo libre.




# Desarrollo técnico correcto y preciso
## app.py

### Considera una lista llamada numeros que contiene elementos como números y cadenas.
```
numeros = [1, 2, "3", 4, "cinco"]
```


### Crea una función llamada calculaDoble() que itere sobre la lista numeros e imprima el doble del valor de cada elemento.
```
def calculaDoble():
    pass
```
### Dentro de la función, utiliza un bloque try-except para manejar los errores que pueden surgir al intentar convertir una cadena a entero.
```
def calculaDoble():
  for numero in numeros:
    try:
      numero = int(numero)  # Intenta convertir el elemento en entero
      print(numero * 2)
    except:
```


### Añade un bloque else para manejar los casos donde la conversión es exitosa, y un bloque finally para ejecutar código que debe ejecutarse en cualquier caso.
```
def calculaDoble():
  for numero in numeros:
    try:
      numero = int(numero)  # Intenta convertir el elemento en entero
      print(numero * 2)
    except:
      print("(no válido)")
    else:
      print("Conversión exitosa")
    finally:
      print("Proceso terminado")
```
### Llama a la función calculaDoble() para ver los resultados.


# Codigo completa

```
numeros = [1, 2, "3", 4, "cinco"]

def calculaDoble():
  for numero in numeros:
    numero = int(numero)  # Intenta convertir el elemento en entero
    print(numero * 2)

def calculaDoble_try_exept():
    for numero in numeros:
        try:
            numero = int(numero)  # Intenta convertir el elemento en entero
            print(numero * 2)
        except:
            print("novalido")
        else:
            print("Conversión exitosa")
        finally:
            print("Proceso terminado")


calculaDoble_try_exept()
```

# Cierre/Conclusión enlazando con la unidad
Este ejercicio demuestra cómo, al trabajar con estructuras de almacenamiento como listas, es fundamental poder manejar datos de tipos distintos sin que el programa falle. El uso de try-except-else-finally