import random


def genera_conjunto():
    conjuntos = set()
    while len(conjuntos) < 9:
        conjuntos.add(random.randint(1, 9))
    return conjuntos

print(genera_conjunto())

def es_correcto(conjuntos):
    conjunto_corecta = {1,2,3,4,5,6,7,8,9}
    if conjunto_corecta == conjuntos:
        return True
    else:
        return False
    
print(es_correcto(genera_conjunto()))

def remove_number(conjuntos):
    numero = random.choice(tuple(conjuntos))
    conjuntos.remove(numero)
    return conjuntos

print(remove_number(genera_conjunto()))
