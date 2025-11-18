import tkinter as tk


vantana = tk.Tk()

#operador1
operador1 = tk.Entry()
operador1.pack(padx=10,pady=10)

#operador2
operador2 = tk.Entry()
operador2.pack(padx=10,pady=10)

#button
boton = tk.Button(text="click para calular")
boton.pack(padx=10,pady=10)

#resultado
resultado = tk.Label(text="Este es resulatdo")
resultado.pack(padx=10,pady=10)




vantana.mainloop() # No te salgas


