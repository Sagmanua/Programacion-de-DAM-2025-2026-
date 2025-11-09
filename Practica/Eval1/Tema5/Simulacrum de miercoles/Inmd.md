
# 1.-Indroduccion brece y contexalizacion





# 2.-Desarrollo técnico correcto y preciso
## Python CRUD 
### Al primero importar `mysql.connector` para puede conectar con Mysql y conecta en bases de datos de mi ordenador y escribir si todo bien or no 

``` 
import mysql.connector
try:
    conexion=mysql.connector.connect(
        host="localhost",
        user="appuser",
        password="m1ClaveSegura!",
        database="portafolio"
    )
    cursor = conexion.cursor()
    print("✅ Conexión exitosa!")
    print("Hola tu redacta database portafolio")
    cursor.close() 
    conexion.close()
except Exception as e:
    print("❌ Error:", e)
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
            print("1.Insertar en tabla de Categoria")
            print("2.Insertar en tabla de Pieza")
            opciondeinsetar = int(input("Escoge una opcion:"))
            if opciondeinsetar == 1:
                break
            elif opciondeinsetar == 2:
                break
            else:
                print("Numero incorecta")
```
#### dentro de esto voy a crear insetar. Da a usario input para escribe su valores despues escribe codigo para gurdar datos en Bases de datos
##### Tabla de Categoria
```
if opciondeinsetar == 1:
                Id_cat = input("Id_cat INT: ")
                titulo_c = input("titulo_c VARCHAR(255): ")
                descripcion_c = input("descripcion_c VARCHAR(255): ")

                cursor.execute(
        '''INSERT INTO Categoria
VALUES ('''+ Id_cat + ''',\'''' + titulo_c + '''\',\'''' + descripcion_c + '''\'
);'''
    )
```
##### Tabla de Pieza
```
elif opciondeinsetar == 2:
                id_pieza = input("id_pieza INT: ")
                titulo_p = input("titulo_p VARCHAR(255): ")
                descripcion_p = input("descripcion_p VARCHAR(255): ")
                imagen = input("imagen: ")
                url = input("url VARCHAR")
                id_categoria = input("id_categoria INT: ")
                cursor.execute('''
                    INSERT INTO Pieza
                    VALUES (
                    '''+id_pieza+''',
                    "''' + titulo_p + '''",
                    "''' + descripcion_p + '''",
                    "''' + imagen + '''",
                    "''' + url + '''",
                    '''+id_categoria+'''
                    );
                ''')
                conexion.commit()
```
### Ahora boy a crear Leidos
#### En Mysql creado view `CatPIEz` por eso solo ajecuta este view
```
elif opcion == 2:
            print("Listamos los clientes")
            cursor.execute("SELECT * FROM CatPIEz")
            resultados = cursor.fetchall()
            for fila in resultados:
                print(fila)
```
### Ahora boy a crear Actulaziones
#### Empezar you tiene 2 tablas  `Pieza` y `Categoria` por eso voy a hacer yna Esoge para usario
```
 print("Escoge una opcion:")
            print("1.Insertar en tabla de Categoria")
            print("2.Insertar en tabla de Pieza")
            opciondeinsetar = int(input("Escoge una opcion:"))
            if opciondeinsetar == 1:
                break
            elif opciondeinsetar == 2:
                break
            else:
                print("Numero incorecta")
```
#### dentro de esto voy a Actuliza. Da a usario input para escribe su valores despues escribe codigo para gurdar datos en Bases de datos


##### Tabla de Categoria
```
if opciondeinsetar == 1:
                Id_cat = input("Id_cat INT: ")
                titulo_c = input("titulo_c VARCHAR(255): ")
                descripcion_c = input("descripcion_c VARCHAR(255): ")

                cursor.execute('''
                    UPDATE Categoria
                    SET titulo_c = "'''+titulo_c+'''",
                        descripcion_c = "'''+descripcion_c+'''"
                    WHERE Id_cat = '''+Id_cat+'''
                ''')
                conexion
```
##### Tabla de Pieza
```
if opciondeinsetar == 2:
                id_pieza = input("id_pieza INT: ")
                titulo_p = input("titulo_p VARCHAR(255): ")
                descripcion_p = input("descripcion_p VARCHAR(255): ")
                imagen = input("imagen: ")
                tiurltulo_p = input("tiurltulo_p: ")
                url = input("url VARCHAR")
                id_categoria = input("id_categoria INT: ")
                cursor.execute('''
                    UPDATE Pieza
                    SET titulo_p = "'''+titulo_p+'''",
                        descripcion_p = "'''+descripcion_p+'''",
                        imagen = "'''+imagen+'''",
                        url = "'''+url+'''",
                        id_categoria = '''+id_categoria+'''
                    WHERE id_pieza = '''+id_pieza+'''
                ''')
```
### Ahora boy a crear Actulaziones
#### Empezar you tiene 2 tablas  `Pieza` y `Categoria` por eso voy a hacer yna Esoge para usario
```
 print("Escoge una opcion:")
            print("1.Insertar en tabla de Categoria")
            print("2.Insertar en tabla de Pieza")
            opciondeinsetar = int(input("Escoge una opcion:"))
            if opciondeinsetar == 1:
                break
            elif opciondeinsetar == 2:
                break
            else:
                print("Numero incorecta")
```
#### dentro de esto voy a Borar. Da a usario input para escribe su valores despues escribe codigo para gurdar datos en Bases de datos


##### Tabla de Categoria
```
if opciondeinsetar == 1:
                print("Eliminamos un ")
                id = input("Introduce el id del cliente que quieres eliminar: ")
                cursor.execute('''
                DELETE FROM Categoria
                WHERE Identificador = '''+id+'''
                ''')
```
##### Tabla de Pieza
```
if opciondeinsetar == 2:
                print("Eliminamos un ")
                id = input("Introduce el id del cliente que quieres eliminar: ")
                cursor.execute('''
                DELETE FROM Pieza
                WHERE Identificador = '''+id+'''
                ''')
```
       

# Codigo Completo

## Python
```
import mysql.connector
try:
    conexion=mysql.connector.connect(
        host="localhost",
        user="appuser",
        password="m1ClaveSegura!",
        database="portafolio"
    )
    cursor = conexion.cursor()
    print("✅ Conexión exitosa!")
    print("Hola tu redacta database portafolio")
    while True:
        print("Escoge una opcion:")
        print("1.-Insertar un cliente")
        print("2.-Listar los clientes")
        print("3.-Actualizar un cliente")
        print("4.-Borrar un cliente")
        opcion = int(input("Escoge una opcion:"))

        if opcion == 1:
            print("Escoge una opcion:")
            print("1.Insertar en tabla de Categoria")
            print("2.Insertar en tabla de Pieza")
            opciondeinsetar = int(input("Escoge una opcion:"))
            if opciondeinsetar == 1:
                Id_cat = input("Id_cat INT: ")
                titulo_c = input("titulo_c VARCHAR(255): ")
                descripcion_c = input("descripcion_c VARCHAR(255): ")

                cursor.execute(
        '''INSERT INTO Categoria
VALUES ('''+ Id_cat + ''',\'''' + titulo_c + '''\',\'''' + descripcion_c + '''\'
);'''
    )
                conexion.commit()
            elif opciondeinsetar == 2:
                id_pieza = input("id_pieza INT: ")
                titulo_p = input("titulo_p VARCHAR(255): ")
                descripcion_p = input("descripcion_p VARCHAR(255): ")
                imagen = input("imagen: ")
                url = input("url VARCHAR")
                id_categoria = input("id_categoria INT: ")

                cursor.execute('''
                    INSERT INTO Pieza
                    VALUES (
                    '''+id_pieza+''',
                    "''' + titulo_p + '''",
                    "''' + descripcion_p + '''",
                    "''' + imagen + '''",
                    "''' + url + '''",
                    '''+id_categoria+'''
                    );
                ''')
                conexion.commit()
            else:
                print("Numero incorecta")
        elif opcion == 2:
            print("Listamos los clientes")
            cursor.execute("SELECT * FROM CatPIEz")
            resultados = cursor.fetchall()
            for fila in resultados:
                print(fila)
        elif opcion == 3:
            print("Escoge una opcion:")
            print("1.Actulizar en tabla de Categoria")
            print("2.Actulizar en tabla de Pieza")
            opciondeinsetar = int(input("Escoge una opcion:"))
            if opciondeinsetar == 1:
                Id_cat = input("Id_cat INT: ")
                titulo_c = input("titulo_c VARCHAR(255): ")
                descripcion_c = input("descripcion_c VARCHAR(255): ")

                cursor.execute('''
                    UPDATE Categoria
                    SET titulo_c = "'''+titulo_c+'''",
                        descripcion_c = "'''+descripcion_c+'''"
                    WHERE Id_cat = '''+Id_cat+'''
                ''')
                conexion.commit()
            if opciondeinsetar == 2:
                id_pieza = input("id_pieza INT: ")
                titulo_p = input("titulo_p VARCHAR(255): ")
                descripcion_p = input("descripcion_p VARCHAR(255): ")
                imagen = input("imagen: ")
                tiurltulo_p = input("tiurltulo_p: ")
                url = input("url VARCHAR")
                id_categoria = input("id_categoria INT: ")
                cursor.execute('''
                    UPDATE Pieza
                    SET titulo_p = "'''+titulo_p+'''",
                        descripcion_p = "'''+descripcion_p+'''",
                        imagen = "'''+imagen+'''",
                        url = "'''+url+'''",
                        id_categoria = '''+id_categoria+'''
                    WHERE id_pieza = '''+id_pieza+'''
                ''')
        elif opcion == 4:
            print("Escoge una opcion:")
            print("1.Actulizar en tabla de Categoria")
            print("2.Actulizar en tabla de Pieza")
            opciondeinsetar = int(input("Escoge una opcion:"))
            if opciondeinsetar == 1:
                print("Eliminamos un ")
                id = input("Introduce el id del cliente que quieres eliminar: ")
                cursor.execute('''
                DELETE FROM Categoria
                WHERE Identificador = '''+id+'''
                ''')
                
            if opciondeinsetar == 2:
                print("Eliminamos un ")
                id = input("Introduce el id del cliente que quieres eliminar: ")
                cursor.execute('''
                DELETE FROM Pieza
                WHERE Identificador = '''+id+'''
                ''')
        else:
            break
    cursor.close() 
    conexion.close()
except Exception as e:
    print("❌ Error:", e)

``` 

# 4.-Cierre/Conclusión enlazando con la unidad