'''
    007 fuerza de dragon
    (c) Bohdan SYdorenko
    Reccorer loa años de produ producción, 
    los meses y los días para contar los patitos de goma producidos diariamente.


'''
'''
Que hago
1.Crea  funcion 
2.return
3.llama a la fubcion  


'''

fuerza = 0
nombre_dragon = None
edad_dragon = 0

nombre_dragon = input("Introduce el nombre de la dragon")
edad_dragon = input("Introduce la edad de la dragon ")

try:
    edad_dragon = int(edad_dragon)
    print("Nombre de tu dragon es ",nombre_dragon,"y su edad es ",edad_dragon)
except:
    edad_dragon = 100
    print("Tu ecribe el edad incorecto por eso edad dragon basico es 100 años por eso \n Nombre de tu dragon es",nombre_dragon,"y su edad es ",edad_dragon)

def class_dragon():
    if edad_dragon <50:
        return  "Joven"
        
    elif edad_dragon >= 50 and edad_dragon <= 199:
        return  "Adulto"
    else:
        return  "Ancion"
        
print(class_dragon())


def entranamiento():
    fuerza = 0
    for dia in range (1,4):
        print ("Dia de entronomeinto",dia)
        if class_dragon() == "Joven":
            fuerza += 2
            print("Fuerza de dragon es ",fuerza)
        elif class_dragon() == "Adulto":
            fuerza += 1
            print("Fuerza de dragon es ",fuerza)
        elif class_dragon() == "Ancion":
            fuerza += 1
            print("Fuerza de dragon es ",fuerza)
    return fuerza
print(entranamiento())
print("Nombre de dragon es ",nombre_dragon,"\nsu edad es",edad_dragon,"\ndepende de su edad su clasifacion es",class_dragon(),"\nSu fuerza depende de entaranamieto es ",entranamiento())