numeros = {1, 2, "3", 4, "cinco","patata"}

print(numeros)
numeros_etiquetas = ["cero", "uno", "dos", "tres", "cuatro", "cinco"]

def calcula_doble(numeros, etiquetas):
    for numero in numeros:
        try:
            n = int(numero)
            print(n * 2)
        except ValueError:
            if numero in etiquetas:
                numero = etiquetas.index(numero)
                print(numero * 2)

calcula_doble(numeros, numeros_etiquetas)
