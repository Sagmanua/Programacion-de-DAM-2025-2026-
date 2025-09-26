class Gato:
    def __init__(self):
        self.color = ""
        self.edad = 0
    def maulla (self):
        print("el gato esta maullando")
    

jaegger = Gato()
jaegger.color = "creme"
jaegger.edad = 9
jaegger.maulla()

print(jaegger)

lana = Gato()
lana.color = "gris"
lana.edad = 13
lana.maulla()