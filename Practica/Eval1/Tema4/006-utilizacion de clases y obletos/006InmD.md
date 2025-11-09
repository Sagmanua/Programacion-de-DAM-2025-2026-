# Indroduccion brece y contexalizacion





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
