import zipfile
import os

origen = 'archivos'
destino = 'archivos.zip'


archivozip = zipfile.ZipFile(destino,'w',zipfile.ZIP_DEFLATED)
for diretorio,carpeta,archivos in os.walk(origen):
    for archivo in archivos:
        rutaarchivo = os.path.join(archivo,archivo)
        rutaarelativa = os.path.realpath(os.path.join(rutaarchivo,origen))
        archivozip.write(rutaarchivo,rutaarelativa)

archivozip.close()