'''
    006-COnstructores
    (c) Bohdan SYdorenko
    En mi tiempo libre, disfruto mucho jugando videojuegos y viendo series anime. Crear objetos utilizando constructores me parece muy interesante porque permite dar forma a mis personajes favoritos como si fueran parte real del juego. En este ejercicio, vamos a utilizar la clase date de Python para crear un objeto que represente la fecha actua'''
'''
Que hago


'''

#import 
import datetime

#variables
Weekday=""

#usa datetime para cojer data de hoy
fecha_actual = datetime.datetime.now()

#imprimir año mes y dia de hoy
print("Hoy es el",fecha_actual.year,fecha_actual.month,fecha_actual.day )

#saber el numero de dia de semana 
day = fecha_actual.weekday()

#probar en que numero es dia 
if day == 0 :
    Weekday = "lunes"
elif day == 1 :
    Weekday = "martes"
elif day == 2 :
    Weekday = "miercoles"
elif day == 3 :
    Weekday = "jueves"
elif day == 4 :
    Weekday = "viernes"
elif day == 5 :
    Weekday = "sábado"
elif day == 6 :
    Weekday = "domingo"
    print("domingo")

#imprimir dia de la semana 
print("Día de la semana:",Weekday )

