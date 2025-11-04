## 1.-Indroduccion brece y contexalizacion
En esta actividad desarrollaremos un programa interactivo en Python llamado “Adivina el número”, cuyo objetivo es que el usuario intente adivinar un número secreto generado por el sistema. Esta práctica se enmarca dentro de la unidad sobre estructuras de control, bucles y manejo de errores, y permite aplicar de manera práctica conceptos teóricos aprendidos en clase.

El juego sirve como contexto para explorar cómo tomar decisiones condicionales, repetir acciones controladas mediante bucles, manejar entradas incorrectas con try/except, y garantizar condiciones válidas mediante aserciones, integrando todo en un programa interactivo y dinámico.




## 2.-Desarrollo técnico correcto y preciso
### 1.imports para puede hacer numero randomo
```
import random
```

### 2.declaras unas variables 
```
intentos = 1
num_guess = 0
max_intentos = 7
       
```
### 3.random numero elegido a computer 
```
numero_guess=random.randint(0, 50)
```
### 4.corecto numero diapasone si es diapasone corecta 
```
assert 0 <= numero_guess <= 50
```
### 5.hoy hacer bucle para intentos 
```
while intentos < max_intentos:
    print("intentos",intentos)
```
### 6.en intento 3 auyda
```
if intentos >= 3:
        #calcula si divedir sin resto o con 
        paridad = numero_guess%2
        #si tiene resto es impar 
        if paridad == 1:
            print("Numero es impar")
        #si no tiene resto es par 
        elif paridad == 0:
            print("Numero es par ")
    #input para usario 
```
### 7.input usario
```
quess_usa = int(input("Introduce de numero"))
```

### 8.probar si numrico esi no skip intento 
```
try:
        #probar si numeor or no 
        quess_usa = int(input("Introduce de numero"))
    except ValueError:
        print("Numero es no numerico probar otrovez  ")
        continue
    
```
### 9.si es mayor or menor or tu gano
```
if numero_guess == quess_usa:
            print("Vamos")
            break
        elif numero_guess > quess_usa:
            print("numero es mas")
        elif numero_guess < quess_usa:
            print("numero es menor")
```
### 10.añade una intrnto cada vez
```
intentos = intentos + 1
```

### 11.tu gano or no y que numero es 
```
print("------------------------")
print("Numero es",numero_guess)
if numero_guess == quess_usa:
    print("Tu gano")
else:
    print("Tu perdió")
``` 

## 3.-Aplicacion practica

```
'''
    Exam tema 3
    (c) Bohdan Sydorenko
    Juego de que es numero 

'''
'''
que hago 
1.imports
2.variables
3.random numero
4.corecto numero diapasone
5.bucle para intentos
6.en intento 3 auyda
7.input usario
8.probar si numrico esi no skip intento 
9.si es mayor or menor or tu gano 
10.tu gano or no y que numero es 



'''

#imports
import random
#variables
intentos = 1
num_guess = 0
max_intentos = 7

#computer elige numeor
numero_guess=random.randint(0, 50)

#probar si es numero correcta 
assert 0 <= numero_guess <= 50

#bucle para intentos 
while intentos < max_intentos :
    
    print("intentos",intentos)
    #en intento 3 pisto
    if intentos >= 3:
        #calcula si divedir sin resto o con 
        paridad = numero_guess%2
        #si tiene resto es impar 
        if paridad == 1:
            print("Numero es impar")
        #si no tiene resto es par 
        elif paridad == 0:
            print("Numero es par ")
    #input para usario 
    try:
        #probar si numeor or no 
        quess_usa = int(input("Introduce de numero"))
        if numero_guess == quess_usa:
            print("Vamos")
            break
        elif numero_guess > quess_usa:
            print("numero es mas")
        elif numero_guess < quess_usa:
            print("numero es menor")
        #si es no numeor skip intento
    except ValueError:
        print("Numero es no numerico probar otrovez  ")
        continue
    #+1 intentos cadad vez 
    intentos = intentos + 1
    

#imprimir si gano or perdido
print("------------------------")
print("Numero es",numero_guess)
if numero_guess == quess_usa:
    print("Tu gano")
else:
    print("Tu perdió")
```

## 4.-Cierre/Conclusión enlazando con la unidad
En esta actividad, hemos aplicado de manera práctica los conceptos fundamentales de la unidad sobre estructuras de control, bucles y manejo de errores en Python. El desarrollo del juego “Adivina el número” nos permitió experimentar cómo la programación combina lógica, validación de datos y control de flujo para crear aplicaciones interactivas y robustas.

Aprendimos que las decisiones condicionales con if/elif/else no solo comparan valores, sino que también guían la interacción con el usuario, mientras que los bucles while nos ayudan a repetir acciones de manera controlada hasta cumplir condiciones específicas. El uso de try/except mostró la importancia de anticipar errores en la entrada de datos, garantizando que el programa no se interrumpa ante situaciones inesperadas.