# Non Playable personaje
import random
import json

class Npc():
    def __init__(self,x,y):
        self.posx = x 
        self.posy = y
    def to_dict(self):
        return {"posx": self.posx, "posy": self.posy}
personajes = []
numero_personajes = 50


for i in range (0,numero_personajes):
    xaleatoria = random.randint(0,500)
    yaleatoria = random.randint(0,500)
    personajes.append(Npc(xaleatoria,yaleatoria))

personajes_json = [p.to_dict() for p in personajes]

print(json.dumps(personajes_json, indent=2))

