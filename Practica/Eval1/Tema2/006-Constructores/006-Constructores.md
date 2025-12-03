```
'''
    006-COnstructores
    (c) Bohdan SYdorenko
    En mi tiempo libre, disfruto mucho jugando videojuegos y viendo series anime. Crear objetos utilizando constructores me parece muy interesante porque permite dar forma a mis personajes favoritos como si fueran parte real del juego. En este ejercicio, vamos a utilizar la clase date de Python para crear un objeto que represente la fecha actua'''
'''
Que hago
1.import 
2.variables
3.Usa datetime
4.imprimir fecha 
5.saber dia numeor del dia 
6.number of dia in palabra 
7.imprimir dia de semana

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
```

##1.-Indroduccion brece y contexalizacion
---
En mi tiempo libre disfruto jugando videojuegos y viendo series anime, actividades que me inspiran a crear objetos y personajes mediante la programación. En este ejercicio aprenderemos a utilizar la clase date del módulo datetime de Python para crear un objeto que represente la fecha actual. A partir de este objeto, podremos obtener y mostrar información importante como el año, el mes, el día y el día de la semana, aplicando conceptos básicos de construcción y manipulación de objetos en Python.



##2.-Desarrollo técnico correcto y preciso
---

1.Import datetime para trabajar con ellos
```
import datetime
```

2.Variables declarar vairiables para trabar luego con ellos
```
Weekday=""
       
```
3.Usa datetime para saber dia mes y año
```
fecha_actual = datetime.datetime.now()
```
4.imprimir fecha de año mes y año
```
print("Hoy es el",fecha_actual.year,fecha_actual.month,fecha_actual.day )


```
5.saber dia numeor del dia para luego puede saber dia de semana sobre este numero
```
day = fecha_actual.weekday()


```
6.number of dia in palabra formula anterior da numero ahora es combrobas con if todo los valores a 0 de 6 
```
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
```
7.imprimir dia de semana
```
print("Día de la semana:",Weekday )
``` 
##-3.-Aplicacion practica
---
```
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
```

##4.-Cierre/Conclusión enlazando con la unidad
---
En este ejercicio aplicamos los conceptos de creación y uso de objetos en Python utilizando el constructor de la clase date del módulo datetime. A través de esta práctica, comprendimos cómo obtener y manipular información relacionada con la fecha actual, empleando atributos y métodos predeterminados. Esta actividad refuerza los conocimientos sobre el uso de constructores en la programación orientada a objetos, demostrando cómo Python permite representar datos reales —como una fecha— mediante instancias de clases predefinidas del propio lenguaje.
