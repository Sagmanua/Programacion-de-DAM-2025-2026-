import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="empresadam",
    password="Empresadam123$",
    database="empresadam"
)
cursor = conexion.cursor()
cursor.execute('''
  INSERT INTO clientes
  VALUES(
    NULL,
    "12345678z",
    "Jose Vicente",
    "Carratala Sanchis",
    "info@jocarsa.com"
  );
''')

conexion.commit()

cursor.close()
conexion.close()

print("1")