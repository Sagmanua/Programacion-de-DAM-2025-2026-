'''
    Aserciones
    (c) Bohdan SYdorenko
    En mi tiempo libre, disfruto mucho jugando videojuegos y viendo películas y series anime. Estos hobbies me ayudan a relajarme y pasar tiempo con amigos. 
    Hoy  hago un ejercicio que combina tus pasatiempos favoritos con el concepto de aserciones en programación.

'''
'''
Que hago
1.variables
2.assert 
3.try
4.exept


'''
#variables

edad = 47


#try para no dar error
try:
    #probar si valor de edad es iqual a 48
    assert edad == 48
    print("edad es correcto")
except:
    #si es edad incorecto 
    print("edad es incorect es no 48 es",edad)