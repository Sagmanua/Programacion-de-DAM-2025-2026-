class Anime():
    def __init__(self,nombre,genero,año_esterno,director):
        self.nombre = nombre
        self.genero = genero
        self.año_esterno = año_esterno
        self.director = director
    def mostrar_info(self):
        print(self.nombre)
        print(self.genero)
        print(self.año_esterno)
        print(self.director)
        print("-----------------------------")


anime1 = Anime("Naruto", "Acción", 2002, "Hayato Date")
anime2 = Anime("Death Note", "Suspenso", 2006, "Tetsurō Araki")
anime3 = Anime("One Piece", "Aventura", 1999, "Konosuke Uda")

anime1.mostrar_info()
anime2.mostrar_info()
anime3.mostrar_info()

anime3.año_estreno = 2000
print("despues de modificar")
anime3.mostrar_info()
