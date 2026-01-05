import random
import json
import math
from flask import Flask, render_template

class Npc:
    def __init__(self, x, y, radio, direccion, velocidad):
        self.posx = x 
        self.posy = y
        self.radio = radio
        self.direccion = direccion
        self.velocidad = velocidad 

    def mover(self):
        self.direccion += (random.random() - 0.5) * 0.2 

        self.posx += math.cos(self.direccion) * self.velocidad
        self.posy += math.sin(self.direccion) * self.velocidad

        if self.posx < 0 or self.posx > 500: self.direccion = math.pi - self.direccion
        if self.posy < 0 or self.posy > 500: self.direccion = -self.direccion

    def to_dict(self):
        return {
            "posx": self.posx,
            "posy": self.posy,
            "radio": self.radio
        }

personajes = [Npc(random.randint(0, 500), random.randint(0, 500), 
                  random.randint(10, 30), random.random()*math.pi*2, 
                  random.random()*5) for _ in range(50)]

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("juego.html")

@app.route("/api")
def api():
    for p in personajes:
        p.mover()
    return json.dumps([p.to_dict() for p in personajes])

if __name__ == "__main__":
    app.run(debug=True)