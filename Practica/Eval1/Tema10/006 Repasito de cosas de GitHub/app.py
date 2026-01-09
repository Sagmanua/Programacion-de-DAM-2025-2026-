nombre_usuario = ""
lista_series = []
lista_peliculas = []

nombre_usuario = input("¡Hola! ¿Cuál es tu nombre? ")
def save_seria():
    while True:
        seria = input("seria")
        if seria.lower() == "fin":
            break
        elif seria.lower() == "si":
            read_seria()
        lista_series.append(seria)
        
    

def read_seria():
    for i in range (len(lista_series)):
        print(lista_series[i])

save_seria()

def save_pelicula():
    while True:
        number = 0
        number =+1
        print(number)
        seria = input("seria")
        if seria.lower() == "fin":
            break
        elif seria.lower() == "si":
            read_pelicula()
        lista_series.append(seria)

def read_pelicula():
    for i in range (len(lista_peliculas)):
        print(lista_peliculas[i])