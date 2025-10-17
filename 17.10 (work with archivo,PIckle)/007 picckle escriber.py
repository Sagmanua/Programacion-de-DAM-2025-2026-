
import pickle

acrchivo = open("datos.bin","wb")

cadena = "Jose Visente"

pickle.dump(cadena,acrchivo)

acrchivo.close