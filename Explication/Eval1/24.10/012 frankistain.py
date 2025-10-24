import tkinter as tk
from tkinter import ttk
import mysql.connector


conexion = mysql.connector.connect(
    host="localhost",
    user="empresadam",
    password="Empresadam123$",
    database="empresadam"
)

ventana = tk.Tk()


# Ejemplo: crear una tabla con ttk.Treeview
arbol = ttk.Treeview(ventana, columns=("dninie","nombre", "apellidos","email"), show="headings")

arbol.heading("dninie", text="DNI/NIE del clientes")
arbol.heading("nombre", text="Nombre del clientes")
arbol.heading("apellidos", text="Apellidos del cliente")
arbol.heading("email", text="Email del cliente")


cursor = conexion.cursor()
cursor.execute('''
    SELECT * FROM clientes;
  );
''')

fillas = cursor.fetchall()
for filla in fillas:
    arbol.insert("","end",value=(filla[1],filla[2],filla[3],filla[4]))

cursor.close()
conexion.close()

arbol.pack(padx=10, pady=10)

ventana.mainloop()
