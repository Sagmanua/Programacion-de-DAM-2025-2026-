
import pickle

acrchivo = open("datos.bin","rb")

cadena =pickle.load(acrchivo)
print(cadena)

acrchivo.close