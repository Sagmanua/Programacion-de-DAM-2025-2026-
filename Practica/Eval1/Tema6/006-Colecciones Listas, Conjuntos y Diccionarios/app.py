personaje = {
    "nombre":"Link",
    "edad":17,
    "fuerza":85,
    "habilidades_especiles":[
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