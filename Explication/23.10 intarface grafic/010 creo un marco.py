import tkinter as tk 

ventana = tk.Tk()
marco = tk.Frame(ventana)
marco.pack(padx=20,pady=20)


tk.Label(marco,text="INtroduce el dni/nie del cliente").pack(padx=20,pady=20)


ventana.mainloop()