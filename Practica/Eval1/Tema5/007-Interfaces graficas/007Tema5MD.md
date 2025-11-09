# Indroduccion brece y contexalizacion
En este contexto, aprenderemos a crear interfaces gráficas interactivas utilizando Python y la biblioteca tkinter. Estas interfaces nos permitirán hacer cosas como calcular operaciones matemáticas o mostrar mensajes cuando se hagan ciertas acciones. Durante mis largas horas jugando videojuegos y disfrutando de las series anime, he aprendido que tener una interfaz visual atractiva puede mejorar la experiencia del usuario. En esta actividad, vamos a crear un microcalculadora sencilla donde los usuarios puedan ingresar dos números y obtener su suma.




# Desarrollo técnico correcto y preciso
## Python
###  Import `tkinter` y cambiar nombre a `tk`. `tkinter` es la interface grafic
```
import tkinter as tk
```
### def para calcular suma de los numeros 
```
def sumar():
    # Obtenemos los valores de las entradas y los convertimos a número
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    resultado = num1 + num2
    etiqueta_resultado.config(text=f"Resultado: {resultado}")
```
### Crear ventana principal
```
ventana = tk.Tk()
ventana.title("Suma de dos números")
```
### Botón para calcular
```
boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.pack()
```

### Etiqueta para mostrar resultado
```
etiqueta_resultado = tk.Label(ventana, text="Resultado: ")
etiqueta_resultado.pack()
```

### Ejecutar el bucle principal
```
ventana.mainloop()
```

###
```
 Crear entradas
entrada1 = tk.Entry(ventana)
entrada1.pack()

entrada2 = tk.Entry(ventana)
entrada2.pack()
```
# Codigo completa

```
import tkinter as tk

# Función para sumar los números
def sumar():
    # Obtenemos los valores de las entradas y los convertimos a número
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    resultado = num1 + num2
    etiqueta_resultado.config(text=f"Resultado: {resultado}")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Suma de dos números")

# Crear entradas
entrada1 = tk.Entry(ventana)
entrada1.pack()

entrada2 = tk.Entry(ventana)
entrada2.pack()

# Botón para calcular
boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.pack()

# Etiqueta para mostrar resultado
etiqueta_resultado = tk.Label(ventana, text="Resultado: ")
etiqueta_resultado.pack()

# Ejecutar el bucle principal
ventana.mainloop()

```

# Cierre/Conclusión enlazando con la unidad
