numeros = {
    1,
    2,
    "3",
    4,
    "cinco"
}

print(numeros)

def caluladoble(numeros):
    for numero in numeros:
        try:
            numero = int(numero)
            print(numero * 2)
        except:
            print("no valido")


caluladoble()