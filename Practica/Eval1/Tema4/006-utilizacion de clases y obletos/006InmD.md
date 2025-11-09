# Indroduccion brece y contexalizacion
En el mundo digital moderno, los videojuegos y las series anime forman parte del entretenimiento diario de millones de personas. Plataformas como Crunchyroll o Netflix permiten seguir cientos de historias diferentes, y los videojuegos narrativos incluso comparten estructuras similares, con capítulos o misiones que se desbloquean progresivamente.
En este ejercicio aprenderemos a modelar una serie anime con una clase en Python, aplicando los conceptos de clases, objetos y métodos, para gestionar de forma sencilla qué episodios hemos visto y cuántos nos quedan por disfrutar.




# Desarrollo técnico correcto y preciso
## Python
### Crear clase `Serias` para gurdar informacion 
```
class Serias():
    self.nombre = nombre
    self.episodios = episodios
```
### gurdar informcaion cuando episodios visto 
```
def ver_episodio(self, episodio):
    self.vistos = episodio
    print("Viendo ",episodio," episodio de ",self.nombre)
```
### calcula cundo episodes restantes para vistar y return este value
```
def episodios_restantes(self):
return self.episodios - self.visto
```
###  Creo la instancia de la clase Series
```
serie = Serias("Attack on Titan", 64)
```
### Simulamos ver el episodio 15
```
serie.ver_episodio(15)
```
### Mostramos cuántos episodios quedan por ver
```
print("Episodios restantes:", serie.episodios_restantes())
```
# Codigo completa
## Python
```
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
```

# Cierre/Conclusión enlazando con la unidad
Este ejercicio muestra cómo las clases y objetos nos permiten representar elementos del mundo real, como una serie anime, dentro de un programa.
De forma similar, en los videojuegos se utilizan clases para crear personajes, niveles o misiones con sus propias propiedades.
Comprender este concepto es fundamental para desarrollar aplicaciones y juegos más organizados y realistas.