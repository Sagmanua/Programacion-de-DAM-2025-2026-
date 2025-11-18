import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="empresadam",
    password="Empresadam123$",
    database="empresadam"
)
cursor = conexion.cursor()
cursor.execute('''
    SELECT * FROM clientes;
  );
''')

fillas = cursor.fetchall()
for filla in fillas:
    print(filla,"")


cursor.close()
conexion.close()
