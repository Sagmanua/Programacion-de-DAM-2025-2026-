'''
    101 SIMULACRUM
    (c) Bohdan Sydorenko
'''
'''
    que hago 
    1.VARIABLES
    2INPUTES
    3.SI EDAD ES MAS QUE 18
    4.SI base_imponible es no negativo
    5.calcular descuento
    6.calcula total_factura
'''




#variables 
clientes_nombre = ""
edad = 0
base_imponible = 0
IVA=0.21
descuento_pct = 0
#inputes 

clientes_nombre=input("Intoduce tu Nombre")
edad=int(input("Introduce tu edad"))


if edad>= 18:
    print("edad es valido")
    base_imponible=float(input("base"))
    
    try:
        base_imponible >= 0
        if base_imponible<100 and base_imponible>0:
            descuento_pct  = 0
            print("Menos de 100 € → 0%")
        elif base_imponible>=100 and base_imponible<199.99:
            descuento_pct  = 5
            print("Entre 100 y 199,99 € → 5%")
        elif base_imponible>=200:
            descuento_pct  = 10
            print("200 € o más → 10%")
    except:
        print("base imponible es negativo")   
    # cálculo del descuento
    importe_descuento = base_imponible*(descuento_pct/100)
    # base después del descuento
    base_tras_descuento = base_imponible-importe_descuento
    # cálculo del IVA
    importe_iva = base_tras_descuento*IVA 
    # total a pagar 
    total_factura = base_tras_descuento+importe_iva 
    
    #imprimir datos de usario
    print("" \
    "Tu nombre es:",clientes_nombre,"" \
    "\nTu edad es:",edad,"" \
    "\nTu base inponible:",base_imponible,\
    "\nTu descuento es:",descuento_pct,"" \
    "\nBase tras descuento:",base_tras_descuento,""
    "\nIVA (21%):",importe_iva,""
    "\nTOTAL A PAGAR:",total_factura)


else:
    print("es menor de 18 ")

