numeros = [1, 2, "3", 4, "cinco"]

def calculaDoble():
  for numero in numeros:
    numero = int(numero)  # Intenta convertir el elemento en entero
    print(numero * 2)

def calculaDoble_try_exept():
    for numero in numeros:
        try:
            numero = int(numero)  # Intenta convertir el elemento en entero
            print(numero * 2)
        except:
            print("novalido")
        else:
            print("Conversión exitosa")
        finally:
            print("Proceso terminado")

calculaDoble_try_exept()