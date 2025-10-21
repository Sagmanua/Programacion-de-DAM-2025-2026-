import zipfile

origen = 'miacrvhivo.txt'

destino = 'comprimindo.zip'

archivo = zipfile.ZipFile(destino,'w')
archivo.write(origen)

