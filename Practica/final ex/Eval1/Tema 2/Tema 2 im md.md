   

## 1.-Indroduccion brece y contexalizacion
Hoy voy a hacer un exam de Tema 2.Viy a hacer creo un script llamado planificador_cuadras.py que calcule cuántas cuadras necesitas en una fecha dada, según el número de caballos y la capacidad de cada cuadra. Debe redondear al alza el número de cuadras, mostrar propiedades de la fecha y presentar un pequeño informe.



## 2.-Desarrollo técnico correcto y preciso

### 1.importo libriria datetima para trabar con fechas y libliria math que usa para calulos 
```
from datetime import datetime
import math
```

### 2.Declara unos varibles 
```
cabalos = 0
capacidad_por_cuadrada = 0
       
```
### 3.Endradas de usario con input saber que quiere usario 
```
cabalos = int(input("Numeros de caballos"))
capacidad_por_cuadrada = int(input("Numros de cuadrados"))
fecha_str = input("Ingrese la fecha (YYYY-MM-DD): ")
```
### 4.convertir fecha de input a varible int para puede trabar con esto 
```
fecha_de_date = datetime.strptime(fecha_str, "%Y-%m-%d").date

```
### 5.Probar si el numro es mas que 0 si no escribir error y no hace hado de codigo 
```
try:
    if cabalos > 0 and capacidad_por_cuadrada > 0:
    print("")
except:
    print("Por favor escibe numero mas que 0 ")

```
### 6.hago calculos de cuadrados 
```
cuadras_necesarias = math.ceil(cabalos/capacidad_por_cuadrada)    
```
### 7.voy a saber que dia de semana a numero eligo usario y comprobar a nombre de semana
```
day = fecha_de_date.isoweekday()
if day == 1 :
            Weekday = "lunes"
        elif day == 2 :
            Weekday = "martes"
        elif day == 3 :
            Weekday = "miercoles"
        elif day == 4 :
            Weekday = "jueves"
        elif day == 5 :
            Weekday = "viernes"
        elif day == 6 :
            Weekday = "sábado"
        elif day == 7 :
            Weekday = "domingo"
            print("domingo")
```
### 8.Imprimir todos y hace un pequino prueba para da sabes usario si su dia es entre semana or fin de semana
```
 print("---------------------------------------")
        print("La fecha ingresada es:", fecha_de_date)
        if day == (1,2,3,4,5):
            prrint("entre semana")
            print("Día de la semana:",Weekday)
        elif day == (6,7):
            print("fin de semana ")
            print("Día de la semana:",Weekday)
        print("Para gurdar nesisito",cuadras_necesarias)
```

## 3.-Aplicacion practica

```
'''
    101 Tema 2 exam
    (c)Bohdan Sydorenko

'''
'''
Que hago:
1.imports
2.variables
3.inputs
4.probar todos inputes 
5.hacer calculos de cuadrados
6.analizar que dia de hoy
7.imprimir todo
'''
#imports 
from datetime import datetime
import math

#variables 
cabalos = 0
capacidad_por_cuadrada = 0




#inputes de usario para coger valores
cabalos = int(input("Numeros de caballos"))
capacidad_por_cuadrada = int(input("Numros de cuadrados"))
fecha_str = input("Ingrese la fecha (YYYY-MM-DD): ")

#convertir fecha de input a varible int 
fecha_de_date = datetime.strptime(fecha_str, "%Y-%m-%d").date()



try:
    if cabalos > 0 and capacidad_por_cuadrada > 0:
        #caluclas cuando nesesito cudrados 
        cuadras_necesarias = math.ceil(cabalos/capacidad_por_cuadrada)
        
        #coger numeor del dia 
        day = fecha_de_date.isoweekday()

        #comprobamos numero de semana con el nimbre del dia 
        if day == 1 :
            Weekday = "lunes"
        elif day == 2 :
            Weekday = "martes"
        elif day == 3 :
            Weekday = "miercoles"
        elif day == 4 :
            Weekday = "jueves"
        elif day == 5 :
            Weekday = "viernes"
        elif day == 6 :
            Weekday = "sábado"
        elif day == 7 :
            Weekday = "domingo"
            print("domingo")


        #Imprimir todos 
        print("---------------------------------------")
        print("La fecha ingresada es:", fecha_de_date)
        if day == (1,2,3,4,5):
            prrint("entre semana")
            print("Día de la semana:",Weekday)
        elif day == (6,7):
            print("fin de semana ")
            print("Día de la semana:",Weekday)
        print("Para gurdar nesisito",cuadras_necesarias)
except:
    print("Por favor escibe numero mas que 0 ")
```

## 4.-Cierre/Conclusión enlazando con la unidad

En esta tarea, reforzamos el uso de objetos de fecha (datetime.date), sus propiedades (año, mes, día, día de la semana, isodía de la semana) y métodos del módulo (math.ceil). Mediante el esquema de entrada-cálculo-salida, aprendimos a realizar validaciones básicas de datos y a presentar los resultados en un informe. La tarea práctica «Planificador estable» demostró cómo aplicar estas herramientas a cálculos y planificación en situaciones reales.