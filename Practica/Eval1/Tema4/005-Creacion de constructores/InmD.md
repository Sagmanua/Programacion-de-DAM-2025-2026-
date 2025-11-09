# Indroduccion brece y contexalizacion
En nuestro mundo digital moderno, los videojuegos y las series anime forman una parte esencial de la cultura pop. Los fans interactúan con personajes, historias y mundos virtuales que muchas veces se inspiran mutuamente. Comprender cómo representar estos elementos mediante programación nos permite modelar digitalmente estos universos y desarrollar aplicaciones que gestionen catálogos, recomendaciones o estadísticas sobre series y videojuegos.




# Desarrollo técnico correcto y preciso
### Crea una clase es le basico que hacer 
```
class Anime:
    pass
```
### Crear proioedades para puedo gurdar inforamcion en clientes 
```
def __init__(self,nombre,genero,año_esterno,director):
        self.nombre = nombre
        self.genero = genero
        self.año_esterno = año_esterno
        self.director = director 
```
### este metodo para visualice los datos del cliente en un formato legible. 
``` 
def mostrar_info(self):
    print(self.nombre)
    print(self.genero)
    print(self.año_esterno)
     print(self.director)
```
### Gurdao informacion en la clases 
```
anime1 = Anime("Naruto", "Acción", 2002, "Hayato Date")
anime2 = Anime("Death Note", "Suspenso", 2006, "Tetsurō Araki")
anime3 = Anime("One Piece", "Aventura", 1999, "Konosuke Uda")
```
### mostrar informacion con def 
```
anime1.mostrar_info()
anime2.mostrar_info()
anime3.mostrar_info()
```
### Cambio datos en la `anime3` y demuestro ella
```
anime3.año_estreno = 2000
print("despues de modificar")
anime3.mostrar_info()
```
# Codigo completa

```
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


anime1 = Anime("Naruto", "Acción", 2002, "Hayato Date")
anime2 = Anime("Death Note", "Suspenso", 2006, "Tetsurō Araki")
anime3 = Anime("One Piece", "Aventura", 1999, "Konosuke Uda")

anime1.mostrar_info()
anime2.mostrar_info()
anime3.mostrar_info()

anime3.año_estreno = 2000
print("despues de modificar")
anime3.mostrar_info()

```

# Cierre/Conclusión enlazando con la unidad
Este ejercicio muestra cómo los constructores con parámetros permiten crear objetos personalizados en programación orientada a objetos. En el contexto del mundo digital moderno, esta técnica es muy útil: por ejemplo, se puede aplicar para desarrollar bases de datos de animes o videojuegos, sistemas de recomendación o catálogos interactivos. Así, la programación se convierte en una herramienta clave para organizar y representar digitalmente la cultura pop que tanto disfrutamos.