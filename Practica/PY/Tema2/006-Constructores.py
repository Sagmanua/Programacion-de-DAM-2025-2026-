'''
    006-COnstructores
    (c) Bohdan SYdorenko
    En nuestra actualidad digital, los videojuegos y las películas son dos de los hobbies más populares entre los jóvenes. Imagina un mundo donde estas actividades forman parte integral del día a día. 
    En este ejercicio, vamos a explorar cómo podemos utilizar objetos predeterminados en el lenguaje de programación para manejar estos hobbies.
'''
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

