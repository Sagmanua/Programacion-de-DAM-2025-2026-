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
