# Indroduccion brece y contexalizacion
Continuando con nuestra exploración de estructuras de almacenamiento en Python, hoy te desafío a trabajar con diccionarios y cómo acceder a sus elementos. El 70% de mi tiempo libre está dedicado a los videojuegos, así que imagina que quieres crear un juego donde cada personaje tenga varias características.






# Desarrollo técnico correcto y preciso
## app.py
### creo un lista 
```
personaje = {
    "nombre": "Link",
    "edad": 17,
    "fuerza": 85,
    "habilidades_especiales": [
        "Ataque giratorio",
        "Uso del arco",
        "Bloqueo con escudo",
        "Resolver acertijos"
    ]
}
```
### imprime `edad` y `nombre` de personaje
```
print(personaje["nombre"])
print(personaje["edad"])
```

### Aumenta en 1 la fuerza del personaje y guarda el nuevo valor.
```
personaje["fuerza"] = personaje["fuerza"] + 1
print(personaje["fuerza"])
```
### Agrega una nueva habilidad a las habilidades especiales de Link u imprimir
```
personaje["habilidades_especiales"].append("Escudo mágico")
print(personaje["habilidades_especiales"])
```
### Elimina una habilidad que no sea útil para el personaje actualmente y imprimir 
```
personaje["habilidades_especiales"].remove("Uso del arco")
print(personaje["habilidades_especiales"])
```

# Codigo completa

```
personaje = {
    "nombre": "Link",
    "edad": 17,
    "fuerza": 85,
    "habilidades_especiales": [
        "Ataque giratorio",
        "Uso del arco",
        "Bloqueo con escudo",
        "Resolver acertijos"
    ]
}

print(personaje["nombre"])
print(personaje["edad"])

personaje["fuerza"] = personaje["fuerza"] + 1
print(personaje["fuerza"])

personaje["habilidades_especiales"].append("Escudo mágico")
print(personaje["habilidades_especiales"])

personaje["habilidades_especiales"].remove("Uso del arco")
print(personaje["habilidades_especiales"])

```

# Cierre/Conclusión enlazando con la unidad
Esta actividad se relaciona directamente con lo aprendido en clase sobre diccionarios y listas, reforzando cómo se pueden combinar para almacenar información más compleja.