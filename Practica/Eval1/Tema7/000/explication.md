# Indroduccion brece y contexalizacion
En mi tiempo libre, disfruto mucho jugando videojuegos, aunque también me apasiona ver películas y series anime como un buen ocio. Además, sigo noticias del fútbol para estar al tanto de los partidos más importantes. Hoy, vamos a trabajar con una clase que combina conceptos de programación y juegos, similar a lo que podría hacer en mis tiempos libres cuando me divierto con videojuegos.




# Desarrollo técnico correcto y preciso
## app.py
### para primero hace imort librias  `math` `json` `random` `flask`
```
import random
import json
import math
from flask import Flask, render_template
```

### crear class `Npc` con  valores `x` `y` `radio` `direccion` `velocidad`
```
class Npc:
    def __init__(self, x, y, radio, direccion, velocidad):
        self.posx = x 
        self.posy = y
        self.radio = radio
        self.direccion = direccion
        self.velocidad = velocidad 
``` 
### en la clase de `Npc` creao funcion `mover` que clacula de movimento de Npc 
```
def mover(self):
    self.direccion += (random.random() - 0.5) * 0.2 

    self.posx += math.cos(self.direccion) * self.velocidad
    self.posy += math.sin(self.direccion) * self.velocidad

    if self.posx < 0 or self.posx > 500: self.direccion = math.pi - self.direccion
    if self.posy < 0 or self.posy > 500: self.direccion = -self.direccion
```
### este es calculo la velocidad de la personaje 
```
self.posx += math.cos(self.direccion) * self.velocidad
self.posy += math.sin(self.direccion) * self.velocidad
```
### caluculo angulo de Npc si es la corner de la box move con negativo de esto movimento
```
if self.posx < 0 or self.posx > 500: self.direccion = math.pi - self.direccion
if self.posy < 0 or self.posy > 500: self.direccion = -self.direccion
```
### en la clase `Npc` creo funcion `to_dict` que conver la valor en formato JSON 
```   
def to_dict(self):
    return {
        "posx": self.posx,
        "posy": self.posy,
        "radio": self.radio
    }
```
### Crear 50 personajes con randomes valores
```
personajes = [Npc(random.randint(0, 500), random.randint(0, 500), 
                  random.randint(10, 30), random.random()*math.pi*2, 
                  random.random()*5) for _ in range(50)]

```
### declara `app` como Flask y crear templates 
```
app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("juego.html")

if __name__ == "__main__":
    app.run(debug=True)
```
### crear ruta api en que gurdar la json file
```
@app.route("/api")
def api():
    for p in personajes:
        p.mover()
    return json.dumps([p.to_dict() for p in personajes])
```
## HTML
### Código básico para una estructura de do
```
<!doctype html>
<html lang="es">
  <head>
    <!-- Añade tu contenido aquí -->
  </head>
  <body>
    <!-- Añade tu contenido aquí -->
  </body>
</html>
```
### Esribo `head` en que guardo configuraciones y enlaces necesarios para que la página funcione y se vea bien, pero no muestra contenido en la pantalla.
```
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Portafolio</title>
    <link rel="stylesheet" href="styles.css">
</head>
```
### Esribo `<body>` que es contiene todo lo que se muestra en la pantalla: encabezado, menú, contenido principal y pie de página y creo la `div` es la personaje y box de 
```
<body>
    <div id="escenario" >
    <div id="personaje" >
        <div id="box" ></div>
    </div>
</div>
</body>
```
### Esribo `<script>` que es contiene el JavaSript codigo dentro de etiqutas 
```
let hoy = new Date();
console.log(hoy);
```
## JS 
### creo un bucle infinito 
```
function bucle() {}
setInterval(bucle, 100);

```
### dentro de bucle coje respusta de la json file 
```
.then(respuesta => respuesta.json())
```

### conventir estos datos en la valores para cada personaje(50)
```
.then(datos => {
    escenario.innerHTML = "";
    datos.forEach(npc => {
        let personaje = document.createElement("div");
        personaje.classList.add("npc");
        personaje.style.left = npc.posx + "px";
        personaje.style.top = npc.posy + "px";
        personaje.style.width = npc.radio + "px";
        personaje.style.height = npc.radio + "px";
        
        personaje.style.backgroundColor = "#" + Math.floor(Math.random() * 16777215).toString(16);
        
        escenario.appendChild(personaje);
```
## CSS 
# Codigo completa
Project/
├─ api/
├─ templates/
│   └─ juego.html
└─ app.py
## app.py
```
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
```
## juego.html
```
<!doctype html>
<html>
  <head>
    <style>
      .npc {
        background: red;
        border-radius: 50%; /* Redondo perfecto */
        position: absolute;
        transition: all 0.1s linear; /* Movimiento suave en 2026 */
      }
      main {
        width: 500px;
        height: 500px;
        border: 1px solid black;
        position: relative;
        overflow: hidden;
      }
    </style>
  </head>
  <body>	
    <main id="escenario"></main>
    <script>
      let escenario = document.querySelector("#escenario")
      
      function bucle() {
        fetch("/api") 
        .then(respuesta => respuesta.json())
        .then(datos => {
            escenario.innerHTML = "";
            datos.forEach(npc => {
                let personaje = document.createElement("div");
                personaje.classList.add("npc");
                personaje.style.left = npc.posx + "px";
                personaje.style.top = npc.posy + "px";
                personaje.style.width = npc.radio + "px";
                personaje.style.height = npc.radio + "px";
                
                personaje.style.backgroundColor = "#" + Math.floor(Math.random() * 16777215).toString(16);
                
                escenario.appendChild(personaje);
            });
        });
      }

      setInterval(bucle, 100);
    </script>
  </body>
</html>
```

# Cierre/Conclusión enlazando con la unidad
Al finalizar este ejercicio, tendrás una comprensión más profunda de cómo manejar objetos con múltiples propiedades y métodos, así como cómo aplicar estos conceptos para crear juegos simples. Este tipo de proyecto puede ser muy divertido y te ayudará a desarrollar habilidades prácticas en programación que podrías utilizar en tus tiempos libres cuando disfrutes jugando videojuegos o cualquier otro juego que necesite un poco de programación detrás.