```
'''
    programa para  informacion a jugador 
    (c) Bohdan Sydorenko 
    este programa pregunta a informacin a jugador 
'''
'''
    Que yo hago
    1. pregunta al usario 
    2. Print un mensaje con su nombre 
    3. pregunta su edad 
    4.calcula su doble edad 
    5. Print su nombre + edad double 


#Variables
nombre_jug = ""
edad_jug = 0
#pregunta la nombre 
nombre_jug = input("hola que tu nombre")
#print nombre de usario
print("Hola ", nombre_jug,"\n")


#pregunta la edad de usario 

edad_jug=input(nombre_jug+"cuando anos tienes\n")

'''
while edad_jug != int(edad_jug):
    try:
        edad_jug = input(int(edad_jug+"\n")) 
        break

    except ValueError:
        print("ecribe numero ")
        edad_jug=input(nombre_jug+"\n cuando anos tienes")
'''

try:
    edad_jug = int(edad_jug)
except:
    print("ecribe numero ")
    edad_jug=input(nombre_jug+"\n cuando anos tienes")
#calclar de double edad de usario 
edad_jug_double = edad_jug*2

#print nombre y eadad de usario 
print(nombre_jug,"tu edad es double es",str(edad_jug_double))
```


1.-Indroduccion brece y contexalizacion

En este ejercicio vamos a dessroolla un ejemplo de indeficar la usario. Aqui nos estudiamos como travaqjer con tipos de datos 

2.-Desarrollo detallado y raeciso 
    1. pregunta al usario que para saber que datos es y para trabajar 
    2. Print un mensaje con su nombre salud con el 
    3. pregunta su edad para saber que datos es y para trabajar 
    4.calcula su doble edad 
    5. Print su nombre + edad double 

3.-Aplicacion practica

```
#Variables
nombre_jug = ""
edad_jug = 0
#pregunta la nombre 
nombre_jug = input("hola que tu nombre")
#print nombre de usario
print("Hola ", nombre_jug,"\n")


#pregunta la edad de usario 

edad_jug=input(nombre_jug+"cuando anos tienes\n")
#print nombre y eadad de usario 
print(nombre_jug,"tu edad es double es",str(edad_jug_double))
```

4.-concuslion 
el ejerciocio permitio aplicar de manera praclica los conceptos basicos de la tipos de datos 
como con ellos trabojo que hace si valores litral pero nesesito numrico para trabajar con ella em matematica

