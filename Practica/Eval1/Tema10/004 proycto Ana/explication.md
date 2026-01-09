# Indroduccion brece y contexalizacion
En nuestro proyecto de mini intérprete Python, vamos a añadir un nuevo endpoint para ejecutar código en múltiples líneas. Este endpoint será útil cuando necesitemos evaluar bloques más grandes de código, como scripts complejos o funciones largas. Además, aprovecharemos este ejercicio para seguir practicando nuestros conocimientos sobre Flask y cómo manejar sesiones.




# Desarrollo técnico correcto y preciso
## 006-nuevo endpoint.py
### import `flask` con `render_template` y `request`


### declara flack name
```
app = Flask(__name__)
```
### create end point `/`
```
@app.route("/")
def inicio():
    return render_template("frente.html")
``` 

### create end point `/api`
```
@app.route("/api")
def api():
    print("He recibido algo")
    return "ok"
```
### create end point `/api/multilinea` En el endpoint /api/multilinea, utiliza la función exec() para ejecutar el código recibido. Crea una variable temporal para almacenar el resultado de la ejecución del código y devuélvelo como respuesta JSON. Asegúrate de capturar cualquier excepción que pueda ocurrir durante la ejecución del código y devolver un mensaje de error con el código 400 (Bad Request).
```
@app.route("/api/multilinea", methods=['POST'])
def multilinea():
    try:
        data = request.get_json(force=True)
        codigo = data.get("code", "")

        local_vars = {}

        exec(codigo, {}, local_vars)

        return {"resultado": local_vars}


    except Exception as e:
        return {"error": str(e)}, 400
```



# Codigo completa

```
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("frente.html")

@app.route("/api")
def api():
    print("He recibido algo")
    return "ok"

@app.route("/api/multilinea", methods=['POST'])
def multilinea():
    try:
        data = request.get_json(force=True)
        codigo = data.get("code", "")

        local_vars = {}

        exec(codigo, {}, local_vars)

        return {"resultado": local_vars}


    except Exception as e:
        return {"error": str(e)}, 400


if __name__ == "__main__":
    app.run(debug=True)


        
    


if __name__ == "__main__":
  app.run(debug=True)
```

# Cierre/Conclusión enlazando con la unidad
Este endpoint permite ejecutar bloques de código más grandes, ampliando la funcionalidad de nuestro mini intérprete. Refuerza conceptos de Flask, manejo de solicitudes POST, JSON y control de errores, mostrando cómo un intérprete puede evolucionar de ejecutar líneas simples a scripts completos de manera segura y práctica.