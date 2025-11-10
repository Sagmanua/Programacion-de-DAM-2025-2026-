import mysql.connector
conexion=mysql.connector.connect(
    host="localhost",
    user="appuser",
    password="m1ClaveSegura!",
    database="portafolioexamen"
)
print("conacta a bases de datos")
cursor = conexion.cursor()
print("Listamos los clientes")
cursor.execute("SELECT * FROM CatPIEz")
resultados = cursor.fetchall()
for fila in resultados:
    print(fila)
