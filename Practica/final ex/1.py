import random

# Variables
intentos = 0
max_intentos = 6

# Computer chooses a number
numero_guess = random.randint(1, 50)
assert 1 <= numero_guess <= 50  # Check invariant

while intentos < max_intentos:
    try:
        quess_usa = int(input(f"Intento {intentos+1}/{max_intentos}. Introduce un número entre 1 y 50: "))
    except ValueError:
        print("Error: debes introducir un número.")
        continue  # Do NOT count this as a try

    if quess_usa < 1 or quess_usa > 50:
        print("Error: número fuera de rango 1-50.")
        continue  # Do NOT count this as a try

    # Only now count the attempt
    intentos += 1
    assert intentos >= 0, "El contador de intentos no puede ser negativo"

    if quess_usa == numero_guess:
        print(f"¡Correcto! Adivinaste el número {numero_guess} en {intentos} intentos.")
        break
    elif quess_usa < numero_guess:
        print("El número es mayor.")
    else:
        print("El número es menor.")

    # Hint after third valid attempt
    if intentos == 3:
        if numero_guess % 2 == 0:
            print("Pista: el número es par.")
        else:
            print("Pista: el número es impar.")
else:
    print(f"Perdiste. El número era {numero_guess}.")
