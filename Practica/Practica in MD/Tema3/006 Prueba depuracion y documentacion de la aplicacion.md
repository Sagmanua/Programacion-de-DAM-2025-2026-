```
'''
    006 Prueba deouracion y documentacion de la aplicion
    (c) Bohdan Sydorenko
    En mi tiempo libre, disfruto mucho jugando videojuegos y viendo películas y series anime. Estos hobbies me ayudan a relajarme y pasar tiempo con amigos.
    Hoy te propongo un ejercicio que combina tus pasatiempos favoritos con el concepto de aserciones en programación.


'''
'''
Que hago
    1.import math para calcular de raiz 
    2.define una funcion con parametro numero en el
    3.probar si es valoe numerico va a segundo paso  si es no es numerico probar convertir a numerico si no va return 0 
    4.comprueba si es no negativo para no da erro si es negativo return 0
    5.ahora calcula raiz y return el
    6.probar todo valor que puede para probar que todo funciona
'''
#import 
import math


#define funcion
def raizSegura(numero):
    #probar si es numerico
    try:
        #transfer a numerico
        numero = float(numero)
        #si es no negativo 
        if numero >= 0:
            #calcula la raiz de numero
            raiz = math.sqrt(numero)
           
            return raiz
        #si es negativo return 0
        else:
            return 0
        
    #si es no numerico return 0 
    except:
        return 0
#probar todos variantes 
print(raizSegura(10)) #numerico
print(raizSegura("10")) #numero literal 
print(raizSegura(-5)) #numerico negativo
print(raizSegura("asdf")) #literal 
```
##1.-Indroduccion brece y contexalizacion
---




##2.-Desarrollo técnico correcto y preciso
---
1.import math para calcular de raiz 

```
import math

```

2.define una funcion con parametro numero en el
```
def raizSegura(numero):

       
```
3.probar si este codigo bien a concreto si este valor es numerico o es literal si es literal puede convertir a numerico  si no va return 0 
```
    try:
        #transfer a numerico
        numero = float(numero)
    except:
        return 0
```
4.comprueba si es no negativo para no da erro si es negativo return 0
```
    if numero >= 0: 
        return raiz
    else:
        return 0

```
5.ahora calcula raiz y return el
```
raiz = math.sqrt(numero)


```
6.probar todo valor que puede para probar que todo funciona
```
print(raizSegura(10)) #numerico
print(raizSegura("10")) #numero literal 
print(raizSegura(-5)) #numerico negativo
print(raizSegura("asdf")) #literal
```

##-3.-Aplicacion practica
---
```
#import 
import math


#define funcion
def raizSegura(numero):
    #probar si es numerico
    try:
        #transfer a numerico
        numero = float(numero)
        #si es no negativo 
        if numero >= 0:
            #calcula la raiz de numero
            raiz = math.sqrt(numero)
           
            return raiz
        #si es negativo return 0
        else:
            return 0
        
    #si es no numerico return 0 
    except:
        return 0
#probar todos variantes 
print(raizSegura(10)) #numerico
print(raizSegura("10")) #numero literal 
print(raizSegura(-5)) #numerico negativo
print(raizSegura("asdf")) #literal 
```

##4.-Cierre/Conclusión enlazando con la unidad
---
