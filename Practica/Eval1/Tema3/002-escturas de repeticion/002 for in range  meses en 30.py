'''
    EStrucluras de repetiocion
    (c) Bohdan SYdorenko
    Reccorer loa años de produ producción, 
    los meses y los días para contar los patitos de goma producidos diariamente.


'''
'''
Que hago
1.crear una buclefor
2.imprimir todo 


'''


for ano in range(1978,2026):
    for mes in [4, 6, 9, 11]: 
        for dia in range(1,32):
            print("Hoy es el dia",dia,"mes",mes,"año",ano)
