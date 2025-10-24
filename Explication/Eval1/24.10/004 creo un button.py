import tkinter as tk 

ventana = tk.Tk()
marco = tk.Frame(ventana)
marco.pack(padx=20,pady=20)

#DNI/NIE
tk.Label(marco,text="INtroduce el dni/nie del cliente").pack(padx=20,pady=20)
dninie = tk.Entry()
dninie.pack(padx=20,pady=20)

#NOMBRE
tk.Label(marco,text="INtroduce el nombre del cliente").pack(padx=20,pady=20)
nombre = tk.Entry()
nombre.pack(padx=20,pady=20)

#APELLIDOS
tk.Label(marco,text="INtroduce el apellidos del cliente").pack(padx=20,pady=20)
apellidos = tk.Entry()
apellidos.pack(padx=20,pady=20)

#EMAIL
tk.Label(marco,text="INtroduce el email del cliente").pack(padx=20,pady=20)
email = tk.Entry()
email.pack(padx=20,pady=20)

tk.Button(marco,text="insertar",command=insertar).pack(padx=20,pady=20)

ventana.mainloop()