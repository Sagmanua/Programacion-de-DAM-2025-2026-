from flask import Flask, render_template, request, jsonify

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