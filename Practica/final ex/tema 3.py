'''
    Exam tema 3
    (c) Bohdan Sydorenko
    Juego de que es numero 

'''
'''
que hago 


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