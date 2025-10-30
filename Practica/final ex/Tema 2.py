'''
    101 Tema 2 exam
    (c)Bohdan Sydorenko

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


fecha_de_date = datetime.strptime(fecha_str, "%Y-%m-%d").date()



try:
    if cabalos > 0 and capacidad_por_cuadrada > 0:
        #caluclas cuando nesesito cudrados 
        cuadras_necesarias = math.ceil(cabalos/capacidad_por_cuadrada)
        

        #fecha de hoy 
        fecha_actual = datetime.now()


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
        print("---------------------------------------")
        print("La fecha ingresada es:", fecha_de_date)
        print("Día de la semana:",Weekday )
        print("Para gurdar nesisito",cuadras_necesarias)
except:
    print("Por favor escibe numero mas que 0 ")
        

