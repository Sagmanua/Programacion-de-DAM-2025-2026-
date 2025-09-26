'''
    aplicacion para soner nombre de dragon y su edad 
    

'''
#entity
nom_dragon_a = input("Nombre de dragon a ")
edad_dragon_a = int(input("Dise el edad de dragon a "))
clas_dragon_a = ""
furza_dragon_a = 0
res_dragon_a = 0

nom_dragon_b = input("Nombre de dragon b ")
edad_dragon_b = int(input("Dise el edad de dragon b "))
clas_dragon_b = ""
furza_dragon_b = 0
res_dragon_b = 0

#try numericos en la edad 
try:
    edad_dragon_a=int(edad_dragon_a)
    
except:
    edad_dragon_a =100
    
    

try:
    edad_dragon_b=int(edad_dragon_b)
except:
    edad_dragon_b =100
    
#clasificasion de dragones por edad    
if edad_dragon_a <50:
    clas_dragon_a="Joven"
elif edad_dragon_a >=50 and edad_dragon_a <=199:
    clas_dragon_a ="Adult"
else :
    clas_dragon_a = "Acion"
print("Clasifacion de dragon a es ",clas_dragon_a)

if edad_dragon_b <50:
    clas_dragon_b="Joven"
elif edad_dragon_b >=50 and edad_dragon_b<=199:
    clas_dragon_b ="Adult"
else :
    clas_dragon_b = "Acion"
print("Clasifacion de dragon a es ",clas_dragon_b)

#simulacion de 3 dias  entrenar de dragones 

for dia in range(1,4):
    #dragon a
    if clas_dragon_a == "Joven":
        furza_dragon_a +=2
        res_dragon_a +=2
    elif clas_dragon_a == "Adult" or clas_dragon_a == "Acion":
        furza_dragon_a +=1
        res_dragon_a +=2
    print("final de dia ",dia,"dragon a \nFurza de dragon a  ",furza_dragon_a,"resestancia de dragon a ",res_dragon_a)
    #dragon b
    if clas_dragon_b == "Joven":
        furza_dragon_b +=2
        res_dragon_b +=2
    elif clas_dragon_b == "Adult" or clas_dragon_a == "Acion":
        furza_dragon_b +=1
        res_dragon_b +=2
    print("final de dia ",dia,"dargon b\nFurza de dragon b  ",furza_dragon_b,"resestancia de dragon b ",res_dragon_b)   