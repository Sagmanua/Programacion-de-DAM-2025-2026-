edad_mago = 0
class_mago = ""
encuado = 15  # energía inicial del escudo
turno = 0
dano = 0
round = 1

# Pedir la edad del mago
edad_mago = input("Introduce la edad del mago: ")

# Convertir la edad a entero, si no se introduce un valor válido, se asigna 100
try:
    edad_mago = int(edad_mago)
except:
    edad_mago = 100 

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

# Imprimir información inicial
print(f"Edad del mago: {edad_mago}")
print(f"Clase del mago: {class_mago}")
print(f"Poder base: {poderBase()}")

# Iniciar la energía del escudo
escudo = 15

# Empezamos el duelo (2 rondas en este caso)
for round in range(1, 3):
    print(f"\nComienza la ronda {round}...")
    
    if round == 1:
        dano = poderBase() // 2  # Daño con hechizo de fuego
        print(f"Turno 1: Hechizo Fuego - Daño infligido: {dano}")
    elif round == 2:
        dano = poderBase() // 3  # Daño con hechizo de rayo
        print(f"Turno 2: Hechizo Rayo - Daño infligido: {dano}")
    
    # Restamos el daño al escudo
    escudo -= dano
    
    # Aseguramos que el escudo no sea negativo
    if escudo < 0:
        escudo = 0
    
    # Imprimir el estado del escudo después de cada turno
    print(f"Energía del escudo: {escudo}")
    
    # Verificar si el escudo ha sido roto
    if escudo == 0:
        print("El mago ha roto el escudo del adversario.")
        break
    else:
        print("El escudo resiste el duelo.")
