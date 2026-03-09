from flask import Flask

app = Flask(__name__)

mensajes = []

@app.route("/")
def inicio():
	global contador
	contador += 1
	return str(mensajes)

if __name__ == "__main__":
	app.run(debug=True)