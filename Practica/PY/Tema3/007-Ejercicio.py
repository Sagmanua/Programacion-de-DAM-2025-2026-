'''
    Estructuro de Salto
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
class_drag = None
fuerza = 0
nombre_dragon = None
edad_dragon = 0

nombre_dragon = input("Introduce el nombre de la dragon")
edad_dragon = input("Introduce la edad de la dragon ")

try:
    edad_dragon = int(edad_dragon)
except:
    edad_dragon = 100
    print("Tu ecribe el edad incorecto por eso edad dragon basico es 100 años")


if edad_dragon <50:
    class_drag = "Joven"
elif edad_dragon >= 50 and edad_dragon <= 199:
    class_drag = "Adulto"
else:
    class_drag = "Ancion"

for dia in range (1,4):
    print ("Dia de entronomeinto",dia)
    if class_drag == "Joven":
        fuerza += 2
        print("Fuerza de dragon es ",fuerza)
    elif class_drag == "Adulto":
        fuerza += 1
        print("Fuerza de dragon es ",fuerza)
    elif class_drag == "Ancion":
        fuerza += 1
        print("Fuerza de dragon es ",fuerza)
print("Nombre de dragon es ",nombre_dragon,"\nsu edad es",edad_dragon,"\ndepende de su edad su clasifacion es",class_drag,"\nSu fuerza depende de entaranamieto es ",fuerza)