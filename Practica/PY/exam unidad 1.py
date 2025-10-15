'''
    v1.0 101 SIMULACRUM
    (c) Bohdan Sydorenko
    Crear un programa en Python que calcule el total de una factura aplicando IVA y un descuento fijo, usando **solo los conceptos de la Unidad 1**.

    
    
    Que nos hacemos 
    1.variables
    2.input
    3.Cálculos
    4.SI aplica Descuente o no 
    5.imprimir todo
    
'''

#Variables 
nombre_cliente = ""
precio_bruto = 0.0
IVA = 0.21
DESCUENTO = 10

#input

nombre_cliente = input("Introduce tu nombre")
precio_bruto=float(input("Escibribe precio bruto"))

#Cálculos

#iva IVA aplicado**:
iva_aplicado = precio_bruto *IVA

#subtotal con IVA
subtotal_iva = precio_bruto + iva_aplicado


#.SI aplica Descuente o no 
if precio_bruto <50:
    DESCUENTO = 0

#Calcula total 
total = subtotal_iva-DESCUENTO

#imprimi todo
print(nombre_cliente,"nombre")
print(precio_bruto,"safasdf")
print("iva_aplicado",iva_aplicado)
print("DESCUENTO",DESCUENTO)
print("total",total)