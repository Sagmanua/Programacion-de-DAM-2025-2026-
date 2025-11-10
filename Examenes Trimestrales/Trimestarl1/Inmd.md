# Indroduccion brece y contexalizacion
En esta Examen trimestrla  se ha explorado el manejo de bases de datos y la importancia de las operaciones CRUD (Crear, Leer, Actualizar y Eliminar) en aplicaciones de software. La práctica desarrollada consiste en una aplicación de consola en Python que permite interactuar directamente con una base de datos MySQL. Esta experiencia brinda una comprensión práctica de cómo se gestionan los datos, se ejecutan consultas y se mantienen la integridad y consistencia de la información en un sistema.




# Desarrollo técnico correcto y preciso
## Python CRUD 
### Import `mysql.connector` pra puede conectar con bases de datos mysql
```
import mysql.connector
```
### Al primero importar `mysql.connector` para puede conectar con Mysql y conecta en bases de datos de mi ordenador y escribir si todo bien or no 

``` 
import mysql.connector
    conexion=mysql.connector.connect(
        host="localhost",
        user="appuser",
        password="m1ClaveSegura!",
        database="portafolio"
    )
    cursor = conexion.cursor()
    print("Hola tu redacta database portafolio")
    cursor.close() 
    conexion.close()
```
### Hacer bucle infinito para crud 
```
    while True:
        pass
```
### Empezar crear CRUD en bucle indinito
```
print("Escoge una opcion:")
print("1.-Insertar un cliente")
print("2.-Listar los clientes")
print("3.-Actualizar un cliente")
print("4.-Borrar un cliente")
opcion = int(input("Escoge una opcion:"))
    if opcion == 1:
        break
    elif opcion == 2:
        break
    elif opcion == 3:
        break
    elif opcion == 4:
        break
    else:
        break
```
### Ahora boy a crear Insetas.
#### Empezar you tiene 2 tablas  `Pieza` y `Categoria` por eso voy a hacer yna Esoge para usario
```
 print("Escoge una opcion:")
            print("1.Insertar en tabla de categoriasportafolio")
            print("2.Insertar en tabla de piezasportafolio")
            opciondeinsetar = int(input("Escoge una opcion:"))
            if opciondeinsetar == 1:
                break
            elif opciondeinsetar == 2:
                break
            else:
                print("Numero incorecta")
```
#### dentro de esto voy a crear insetar. Da a usario input para escribe su valores despues escribe codigo para gurdar datos en Bases de datos
##### Tabla de categoriasportafolio
```
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

```
##### Tabla de piezasportafolio
```
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
```
### Ahora boy a crear Leidos
#### En Mysql creado listar `categoriasportafolio` y `piezasportafolio` view `CatPIEz` por eso solo ajecuta este view
```
elif opcion == 2:
            print("Listamos los clientes")
            print("1.Listamos la tabla de categoriasportafolio ")
            print("2.Listamos la tabla de piezasportafolio ")
            print("3.Listamos la vista de los w tablas ")
            if opcionlistar == 1:
                pass
            elif opcionlistar == 2:
                pass
            elif opcionlistar == 3:
                pass
            else:
                 print("Numeor incorecta")
```
##### Listar de tabla de categoriasportafolio
```
if opcionlistar == 1:
    cursor.execute("SELECT * FROM categoriasportafolio")
    resultados = cursor.fetchall()
    for fila in resultados:
    print(fila)
```
##### Listar de tabla de piezasportafolio
```
elif opcionlistar == 2:
    cursor.execute("SELECT * FROM piezasportafolio")
    resultados = cursor.fetchall()
    for fila in resultados:
    print(fila)
```
#####
```
elif opcionlistar == 3:
    cursor.execute("SELECT * FROM CatPIEz")
    resultados = cursor.fetchall()
    for fila in resultados:
                    print(fila)
```
### Ahora boy a crear Actulaziones
#### Empezar you tiene 2 tablas  `piezasportafolio` y `categoriasportafolio` por eso voy a hacer yna Esoge para usario
```
 print("Escoge una opcion:")
            print("1.Insertar en tabla de categoriasportafolio")
            print("2.Insertar en tabla de piezasportafolio")
            opciondeinsetar = int(input("Escoge una opcion:"))
            if opciondeinsetar == 1:
                break
            elif opciondeinsetar == 2:
                break
            else:
                print("Numero incorecta")
```
#### dentro de esto voy a Actuliza. Da a usario input para escribe su valores despues escribe codigo para gurdar datos en Bases de datos


##### Tabla de categoriasportafolio
```
if opciondeinsetar == 1:
                Identificador_categoria = input("Identificador_categoria INT: ")
                nombre = input("nombre VARCHAR(255): ")

                cursor.execute('''
                    UPDATE categoriasportafolio
                    SET nombre = "'''+nombre+'''"
                    WHERE Identificador_categoria = '''+Identificador_categoria+'''
                ''')
                conexion.commit()
```
##### Tabla de piezasportafolio
```
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
```
### Ahora boy a crear Actulaziones
#### Empezar you tiene 2 tablas  `piezasportafolio` y `categoriasportafolio` por eso voy a hacer yna Esoge para usario
```
 print("Escoge una opcion:")
            print("Escoge una opcion:")
            print("1.Actulizar en tabla de categoriasportafolio")
            print("2.Actulizar en tabla de Pieza")
            if opciondeinsetar == 1:
                break
            elif opciondeinsetar == 2:
                break
            else:
                print("Numero incorecta")
```
#### dentro de esto voy a Borar. Da a usario input para escribe su valores despues escribe codigo para gurdar datos en Bases de datos


##### Tabla de categoriasportafolio
```
if opciondeinsetar == 1:
                print("Eliminamos un ")
                Identificador_categoria = input("Introduce el id del cliente que quieres eliminar: ")
                cursor.execute('''
                DELETE FROM categoriasportafolio
                WHERE Identificador_categoria = '''+Identificador_categoria+'''
                ''')
```
##### Tabla de piezasportafolio
```
if opciondeinsetar == 2:
                print("Eliminamos un ")
                Identificador_portfolio = input("Introduce el id del cliente que quieres eliminar: ")
                cursor.execute('''
                DELETE FROM piezasportafolio
                WHERE Identificador_portfolio = '''+Identificador_portfolio+'''
                ''')
```

# Codigo completa

```
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
```

# Cierre/Conclusión enlazando con la unidad
La implementación de esta aplicación CRUD ha permitido consolidar los conceptos aprendidos en la unidad sobre bases de datos y programación. Se evidenció cómo las operaciones básicas de manipulación de datos se integran en un flujo lógico de la aplicación, reforzando la importancia de la interacción entre Python y MySQL para gestionar información de manera eficiente y segura. Esta práctica contribuye a preparar al estudiante para el desarrollo de soluciones más complejas, aplicando los principios de la unidad en un contexto real y funcional.