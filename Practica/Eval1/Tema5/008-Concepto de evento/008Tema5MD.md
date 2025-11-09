# Indroduccion brece y contexalizacion
El ejercicio consiste en crear una pequeña aplicación de gestión de clientes utilizando Python, MySQL y Tkinter. Se relaciona con mis hobbies y pasatiempos en programación y videojuegos, ya que disfruto creando interfaces gráficas y gestionando datos de manera interactiva. Al desarrollar esta práctica, puedo aplicar mis intereses en automatización y desarrollo de pequeñas herramientas, lo que hace el aprendizaje más entretenido y cercano a mi vida diaria.


# Desarrollo técnico correcto y preciso
## Python
### Import `tkinter` y cambiar nombre a `tk`. `tkinter` es la interface grafic.
```
import tkinter as tk
``` 
### Import `Mysql` para podria conectar a mysql databases
```
import mysql.connector
```
### Conecta a bases datos en ni caso `empresadam` con user `empresadam` y contrasena `Empresadam123$`
# Codigo completa

```
import tkinter as tk
import mysql.connector
conexion = mysql.connector.connect(
    host="localhost",
    user="empresadam",
    password="Empresadam123$",
    database="empresadam"
    )
cursor = conexion.cursor()
ventana = tk.Tk()
def insertar():
  cursor.execute('''
    INSERT INTO clientes
    VALUES(
      NULL,
      "'''+dninie.get()+'''",
      "'''+nombre.get()+'''",
      "'''+apellidos.get()+'''",
      "'''+email.get()+'''"
    );
  ''')
  conexion.commit()
marco = tk.Frame(ventana)
tk.Label(marco,text="Introduce el dni/nie del cliente").pack(padx=10,pady=10)
dninie = tk.Entry(marco)
dninie.pack(padx=10,pady=10)
tk.Label(marco,text="Introduce el nombre del cliente").pack(padx=10,pady=10)
nombre = tk.Entry(marco)
nombre.pack(padx=10,pady=10)
tk.Label(marco,text="Introduce los apellidos del cliente").pack(padx=10,pady=10)
apellidos = tk.Entry(marco)
apellidos.pack(padx=10,pady=10)
tk.Label(marco,text="Introduce el email del cliente").pack(padx=10,pady=10)
email = tk.Entry(marco)
email.pack(padx=10,pady=10)
tk.Button(marco,text="Insertar cliente",command = insertar).pack(padx=10,pady=10)
marco.pack(padx=20,pady=20)
ventana.mainloop()
```

# Cierre/Conclusión enlazando con la unidad


Esta actividad integra conceptos aprendidos en la unidad sobre bases de datos, interfaces gráficas y programación orientada a eventos. Me ha permitido comprender cómo conectar una aplicación con una base de datos, recoger información del usuario y mostrarla dinámicamente. En el futuro, puedo aplicar estos conceptos para crear herramientas interactivas, programas de gestión o aplicaciones que automaticen tareas cotidianas, combinando lógica de programación con presentación visual.