'''

 Calcula el poder base del mago según su edad.

    Parámetros:
    edad (int): Edad del mago.

    Retorna:
    int: Poder base correspondiente al rango del mago.
'''
edad_mago = 0
class_mago = ""
#poderBase = 0
encuado = 15 
turno = 0
dano = 0
round = 1

#pedir la edad 
edad_mago= input("edad de mago")

#convertir a entero
try:
    edad_mago = int(edad_mago)
#si falta edad 100
except:
    edad_mago = 100 

# clasifica por edad

    # menor que 30 es Aprendiz
# Clasificación del mago según su edad
if edad_mago < 30:
    class_mago = "Aprendiz"
elif 30 <= edad_mago <= 99:
    class_mago = "Hechicero"
else:
    class_mago = "Archimago"

# Función que devuelve el poder base según el tipo de mago
def poderBase():
    if class_mago == "Aprendiz":
        return 5
    elif class_mago == "Hechicero":
        return 8
    elif class_mago == "Archimago":
        return 10

# Ahora, después de clasificar al mago, puedes llamar a poderBase sin problemas
dano = poderBase() // 2  # Ahora class_mago está correctamente definido

# empezamos bucle

# recorre dos turnos con for

for rounds in range (1,3):
    print("empesar la fight")
    # turno 1 fuego daño = poderBase // 2

    if rounds == 1:
        
        dano = poderBase() // 2
        print("round1")
        print (dano)
        encuado = encuado-dano
    # turno 2 hechizo rayo = daño = poderBase // 3

    elif rounds == 2:
        dano = poderBase() // 3
        print ("round2")
        print(dano)
        encuado = encuado-dano
    
# si energia escudo baja de cero, ajusta a cero

if encuado<0:
   encuado = 0 

# resta el daño al escudo
    
print(encuado,"este es la hp de encuado")



print("\n--- Resultado del Duelo ---")
print(f"Edad del mago: {edad_mago}")
print(f"Rango: {class_mago}")
print(f"Poder base: {poderBase()}")
print(f"Energía final del escudo: {encuado}")

# tras cada daño, print de daño y mayor que cero
# tras ajuste energia, print y energia es mayor que cero

# salida: edad, rango, poder base, energia del escudo
# energia es cero, mago rompe escudo
# energia mayor que cero, escudo resiste duelo
