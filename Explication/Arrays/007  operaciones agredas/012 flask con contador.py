import random
from flask import Flask,render_template

from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def inicio():
    contador = 0
    patron = {1,2,3,4,5,6,7,8,9}
    sudoku = []

    for celda in range(9):
        while True:
            contador += 1
            lista = [random.randint(1,9) for _ in range(9)]
            if set(lista) == patron:
                sudoku.append(lista)
                break

    print("He necesitado, con fuerza bruta, " + str(contador) + " intentos")
    return render_template("index.html", datos=sudoku)

if __name__ == "__main__":
    app.run(debug=True)

