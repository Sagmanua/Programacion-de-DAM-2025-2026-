import mysql.connector
conexion=mysql.connector.connect(
    host="localhost",
    user="appuser",
    password="m1ClaveSegura!",
    database="portafolioexamen"
)
print("conacta a bases de datos")
print("Hola tu redacta database portafolio")
while True:
    print("Escoge una opcion:")
    print("1.-Insertar un cliente")
    print("2.-Listar los clientes")
    print("3.-Actualizar un cliente")
    print("4.-Borrar un cliente")
    opcion = int(input("Escoge una opcion:"))

    cursor = conexion.cursor()
    print("Listamos los clientes")
    cursor.execute("SELECT * FROM CatPIEz")
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)
    if opcion == 1:
            print("Escoge una opcion:")
            print("1.Insertar en tabla de categoriasportafolio")
            print("2.Insertar en tabla de piezasportafolio")
            opciondeinsetar = int(input("Escoge una opcion:"))
            if opciondeinsetar == 1:
                Identificador_categoria = input("Id_cat INT: ")
                nombre = input("titulo_c VARCHAR(255): ")
                cursor.execute('''
                    INSERT INTO categoriasportafolio
                    VALUES (
                    '''+Identificador_categoria+''',
                    "''' + nombre + '''"
                    );
                ''')
                conexion.commit()
            elif opciondeinsetar == 2:
                Identificador_portfolio = input("id_pieza INT: ")
                titulo = input("titulo_p VARCHAR(255): ")
                descripcion = input("descripcion_p VARCHAR(255): ")
                fecha = input("fecha: ")
                id_categoria = input("id_categoria INT: ")

                cursor.execute('''
                    INSERT INTO piezasportafolio
                    VALUES (
                    '''+Identificador_portfolio+''',
                    "''' + titulo + '''",
                    "''' + descripcion + '''",
                    "''' + fecha + '''",
                    '''+id_categoria+'''
                    );
                ''')
                conexion.commit()
            else:
                print("Numero incorecta")
    elif opcion == 2:

            print("Listamos los clientes")
            print("1.Listamos la tabla de categoriasportafolio ")
            print("2.Listamos la tabla de piezasportafolio ")
            print("3.Listamos la vista de los w tablas ")
            opcionlistar = int(input("Escoge una opcion:"))
            if opcionlistar == 1:
                cursor.execute("SELECT * FROM categoriasportafolio")
                resultados = cursor.fetchall()
                for fila in resultados:
                    print(fila)
            elif opcionlistar == 2:
                cursor.execute("SELECT * FROM piezasportafolio")
                resultados = cursor.fetchall()
                for fila in resultados:
                    print(fila)
            elif opcionlistar == 3:
                cursor.execute("SELECT * FROM CatPIEz")
                resultados = cursor.fetchall()
                for fila in resultados:
                    print(fila)
            else:
                 print("Numeor incorecta")
    elif opcion == 3:
            print("Escoge una opcion:")
            print("1.Actulizar en tabla de categoriasportafolio")
            print("2.Actulizar en tabla de Pieza")
            opciondeinsetar = int(input("Escoge una opcion:"))
            if opciondeinsetar == 1:
                Identificador_categoria = input("Identificador_categoria INT: ")
                nombre = input("nombre VARCHAR(255): ")

                cursor.execute('''
                    UPDATE categoriasportafolio
                    SET nombre = "'''+nombre+'''"
                    WHERE Identificador_categoria = '''+Identificador_categoria+'''
                ''')
                conexion.commit()
            if opciondeinsetar == 2:
                Identificador_portfolio = input("Identificador_portfolio INT: ")
                titulo = input("titulo VARCHAR(255): ")
                descripcion = input("descripcion VARCHAR(255): ")
                fecha = input("fecha: ")
                tiurltulo_p = input("tiurltulo_p: ")
                id_categoria = input("id_categoria INT: ")
                cursor.execute('''
                    UPDATE piezasportafolio
                    SET titulo = "'''+titulo+'''",
                        descripcion_p = "'''+descripcion+'''",
                        fecha = "'''+fecha+'''",
                        id_categoria = '''+id_categoria+'''
                    WHERE Identificador_portfolio = '''+Identificador_portfolio+'''
                ''')


    elif opcion == 4:
            print("Escoge una opcion:")
            print("1.Actulizar en tabla de categoriasportafolio")
            print("2.Actulizar en tabla de Pieza")
            opciondeinsetar = int(input("Escoge una opcion:"))
            if opciondeinsetar == 1:
                print("Eliminamos un ")
                Identificador_categoria = input("Introduce el id del cliente que quieres eliminar: ")
                cursor.execute('''
                DELETE FROM categoriasportafolio
                WHERE Identificador_categoria = '''+Identificador_categoria+'''
                ''')
                
                conexion.commit()
            if opciondeinsetar == 2:
                print("Eliminamos un ")
                Identificador_portfolio = input("Introduce el id del cliente que quieres eliminar: ")
                cursor.execute('''
                DELETE FROM piezasportafolio
                WHERE Identificador_portfolio = '''+Identificador_portfolio+'''
                ''')
    else:
            break