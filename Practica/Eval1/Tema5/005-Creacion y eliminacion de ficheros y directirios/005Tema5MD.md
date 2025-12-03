# Indroduccion brece y contexalizacion
En mi tiempo libre, disfruto jugando videojuegos y siguiendo series anime. Ambos hobbies requieren creatividad y atención al detalle, habilidades que también son muy útiles en programación. En este ejercicio, vamos a aplicar lo aprendido en clase para crear, comprimir y eliminar archivos usando Python, simulando un flujo de trabajo que podría ser útil, por ejemplo, para organizar archivos de partidas guardadas o listas de episodios.

# Desarrollo técnico correcto y preciso
## Python
### import `zipfile` para compression las archivos
```
import zipfile
```
### Elige archivo i nobre despues de compression
```
origen = 'miacrvhivo.txt'

destino = 'basededatos.zip'
```
### compression archivo 
```
archivo = zipfile.ZipFile(destino, 'w', compression=zipfile.ZIP_DEFLATED)
archivo.write(origen)
```

# Codigo completa

```
import zipfile

origen = 'miacrvhivo.txt'

destino = 'basededatos.zip'

archivo = zipfile.ZipFile(destino, 'w', compression=zipfile.ZIP_DEFLATED)
archivo.write(origen)

```

# Cierre/Conclusión enlazando con la unidad
Este ejercicio nos permite practicar la manipulación de archivos y la compresión usando Python, aplicando lo aprendido en clase de manera práctica. Además, se relaciona con mis hobbies porque organizar archivos de manera eficiente puede ser útil para guardar partidas, registros de anime vistos o cualquier contenido digital que manejemos. Así, la programación se vuelve una herramienta que mejora y facilita la gestión de nuestras actividades recreativas.