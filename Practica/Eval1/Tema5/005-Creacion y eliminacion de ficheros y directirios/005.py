import zipfile

origen = 'miacrvhivo.txt'

destino = 'basededatos.zip'

archivo = zipfile.ZipFile(destino, 'w', compression=zipfile.ZIP_DEFLATED)
archivo.write(origen)