
```
'''
    v0.1 Exam final
    (c) 2025 Bohdan Sydorenko
    Crear un programa en Python que calcule el total de una factura aplicando IVA y un descuento fijo, usando **solo los conceptos de la Unidad 1**
'''
'''
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
print("------------RESUME--------------")
print("Tu Nombre es",nombre_cliente)
print("tu presio bruto es",precio_bruto)
print("Tu iva aplicado es ",iva_aplicado)
print("Tu descuento es ",DESCUENTO)
print("Total que pagar ",total)
```  
    




##1.-Indroduccion brece y contexalizacion
---
Se calculará al cliente el monto total que debe pagar, con consideración del IVA y un descuento que viene incluido bajo un condición específica en este ejercicio.

Este ejercicio ayuda a fortalecer principios básicos de programación, como la utilización de constantes, operadores aritméticos, variables y estructuras condicionales.



##2.-Desarrollo técnico correcto y preciso
---

1.variables declarams variables para trabar con ellos 
```
nombre_cliente = ""
precio_bruto = 0.0
IVA = 0.21
DESCUENTO = 10

```

2.input para usario introduce sus datos y programa puede trabar con ellos  
```
nombre_cliente = input("Introduce tu nombre")
precio_bruto=float(input("Escibribe precio bruto"))
       
```
3.Cálculos 
```
#iva IVA aplicado**:
iva_aplicado = precio_bruto *IVA

#subtotal con IVA
subtotal_iva = precio_bruto + iva_aplicado
```
4.SI aplica Descuente o no. Si precio_bruto mas de 50 no cambia nada y total calculas con descuente 10 si es menos de 50 no tiene DESCUENTO i valor de descuente es 0 
```
if precio_bruto <50:
    DESCUENTO = 0

#Calcula total 
total = subtotal_iva-DESCUENTO

```
5.imprimir todo
```
print("------------RESUME--------------")
print("Tu Nombre es",nombre_cliente)
print("tu presio bruto es",precio_bruto)
print("Tu iva aplicado es ",iva_aplicado)
print("Tu descuento es ",DESCUENTO)
print("Total que pagar ",total)

```


##-3.-Aplicacion practica
---
```
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
print("------------RESUME--------------")
print("Tu Nombre es",nombre_cliente)
print("tu presio bruto es",precio_bruto)
print("Tu iva aplicado es ",iva_aplicado)
print("Tu descuento es ",DESCUENTO)
print("Total que pagar ",total)
```

##4.-Cierre/Conclusión enlazando con la unidad
---
Este ejercicio facilita consolidar los conceptos de la unidad respecto a estructuras condicionales, variables, constantes y operadores, al aplicárselos a un ejemplo práctico de factura.
Facilita comprender cómo se puede automatizar cálculos como el IVA, los descuentos y el monto a pagar al combinar teoría con un caso específico de programación.

