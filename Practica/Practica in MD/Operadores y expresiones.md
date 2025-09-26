
```
'''
    Calculador de IVA
    (c) Bohdan Sydorenko


'''

'''
Que hago

1. crear variables 
2.intritudece de la  factura (input)
3.calcular de IVA
4.Print 

'''
#Variables
Iva = 0.21
base_imponible = 0.0
total_iva= 0
total_factura = 0

#Importe de las datos
base_imponible = float(input("Intorudce de tu imponible "))

#calculador
total_iva = base_imponible * Iva 

total_factura = base_imponible + total_iva

#imprir 
print("Base imponible",base_imponible,
      "\n Iva (21%)",total_iva,
       "\n Total factura", total_factura )
```
---
##1.-Indroduccion brece y contexalizacion
---
Every time we purchase a good or service in daily life, we must pay an additional tax to the base price known as IVA (Impuesto sobre el Valor Añadido).
##2.-Desarrollo técnico correcto y preciso
1. crear variables
```
Iva = 0.21
base_imponible = 0.0
total_iva= 0
total_factura = 0
```
2.intritudece de la  factura (input)
```
base_imponible = float(input("Intorudce de tu imponible "))

```
3.calcular de IVA
```
total_iva = base_imponible * Iva 

total_factura = base_imponible + total_iva

```
4.Print 
```
print("Base imponible",base_imponible,
      "\n Iva (21%)",total_iva,
       "\n Total factura", total_factura )
```
##-3.-Aplicacion practica
```
#Variables
Iva = 0.21
base_imponible = 0.0
total_iva= 0
total_factura = 0

#Importe de las datos
base_imponible = float(input("Intorudce de tu imponible "))

#calculador
total_iva = base_imponible * Iva 

total_factura = base_imponible + total_iva

#imprir 
print("Base imponible",base_imponible,
      "\n Iva (21%)",total_iva,
       "\n Total factura", total_factura
```

##4.-Cierre/Conclusión enlazando con la unidad
Como se ha evidenciado, la programación hace posible que cálculos diarios, como el IVA, sean hechos de manera rápida y exacta. Esta práctica consolida la utilización de operadores aritméticos, variables y entrada/salida de datos en Python, estableciendo así las bases para tareas más complejas en unidades subsiguientes. Asimismo, se contextualiza con sucesos reales, evidenciando la aplicabilidad práctica de la programación en el día a día.

