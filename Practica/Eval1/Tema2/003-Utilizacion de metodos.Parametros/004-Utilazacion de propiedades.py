'''
    Utilazacion de propiedades
    (c) Bohdan SYdorenko
    En nuestra sociedad actual, los videojuegos y las películas son dos entretenimientos populares que muchas personas disfrutan. 
    Este enfoque te permitirá experimentar con la manipulación de propiedades de objetos utilizando un lenguaje de programación como Python.



'''
'''
Que hago
1.crear class Pelicula
2.dar valores a propieda Pelicula
3.crear class Videojuego
4.dar valores a propieda VideoJuego
5.Imprimir propiedades con su volores

'''
 
#crear class Pelicula
class Pelicula:
    def __init__(self,nombre,director,anyo_estreno):
        self.nombre = nombre
        self.director = director
        self.anyo_estreno = anyo_estreno

#dar valores a propieda Pelicula
pelicula = Pelicula("El Señor de los Anillos: La comunidad del anillo","Peter Jackson",2001)


#crear class Videojuego
class Videojuego:
    def __init__(self,nombre,desarrollador,anyo_lanzamiento):
        self.nombre = nombre
        self.desarrollador = desarrollador
        self.anyo_lanzamiento = anyo_lanzamiento
#dar valores a propieda VideoJuego
juego = Videojuego("Minecraft","Mojang Studios",2009)

#Imprimir propiedades con su volores
print(juego.nombre, "\n",juego.desarrollador,"\n",juego.anyo_lanzamiento)
print(pelicula.nombre, "\n",pelicula.director,"\n",pelicula.anyo_estreno)
