import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()


# Ejemplo: crear una tabla con ttk.Treeview
arbol = ttk.Treeview(ventana, columns=("nombre", "apellidos"), show="headings")
arbol.heading("nombre", text="Nombre del clientes")
arbol.heading("apellidos", text="Apellidos del cliente")

arbol.insert("", "end", values=("Bohdan", "Sydorenko"))
arbol.insert("", "end", values=("Juan", "GArcia"))
arbol.pack(padx=10, pady=10)

ventana.mainloop()
