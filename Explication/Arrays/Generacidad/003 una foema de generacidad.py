numeros = {
    1,
    2,
    "3",
    4
}

print(numeros)

def caluladoble():
    for numero in numeros:
        numero = int(numero) 
        print(numero*2) 

caluladoble()