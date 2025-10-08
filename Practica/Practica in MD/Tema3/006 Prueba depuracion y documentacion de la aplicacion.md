```
'''
    Ejercicio de final de unidad
    (c) Bohdan Sydorenko
    En mi tiempo libre, disfruto mucho jugando videojuegos y viendo series anime. 
    Esta actividad son una gran parte de mi diversión y me mantienen entretenido cuando no estoy ocupado con mis estudios.


'''
'''
Que hago
    1.variables
    2.declarar varibles
    3.calcula las goeas de video juegos
    4.calculas las horas de episodios 
    5.imprimir todo
'''

#import 
import math
#variable





def raizSegura(numero):

    try:
        numero = float(numero)
        
        if numero >= 0:
            raiz = math.sqrt(numero)
            #print(raiz)
            return raiz
        else:
            return 0
        
        
    except:
        return 0

print(raizSegura(10))
print(raizSegura("10"))
print(raizSegura(-5))
print(raizSegura("asdf"))
```
