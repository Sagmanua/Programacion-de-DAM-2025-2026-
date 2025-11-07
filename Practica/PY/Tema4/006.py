class Serias():
    def __init__ (self,nombre,episodios):
        self.nombre = nombre
        self.episodios = episodios
    def ver_episodio(self, episodio):
            self.vistos = episodio
            print("Viendo ",episodio," episodio de ",self.nombre)
    def episodios_restantes(self):
        return self.episodios - self.vistos
# Creamos la instancia de la clase Series
serie = Serias("Attack on Titan", 64)

# Simulamos ver el episodio 15
serie.ver_episodio(15)

# Mostramos cuántos episodios quedan por ver
print("Episodios restantes:", serie.episodios_restantes())


