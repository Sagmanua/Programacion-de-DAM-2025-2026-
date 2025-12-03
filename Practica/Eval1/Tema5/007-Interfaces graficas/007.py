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
