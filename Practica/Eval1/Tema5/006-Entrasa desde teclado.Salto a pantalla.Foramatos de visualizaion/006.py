class Cliente:
    def __init__(self, nombre, edad, correo, videojuego_favorito):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.videojuego_favorito = videojuego_favorito

    def mostrar(self):
        print(self.nombre, "-", 
              self.edad, "años -", 
              self.correo, "-", "Juego:", 
              self.videojuego_favorito)

clientes = []

while True:
    print("1. Añadir cliente")
    print("2. Mostrar clientes")
    print("3. Buscar por videojuego")
    print("4. Salir")
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        nombre = input("Nombre")
        edad = input("Edad")
        correo = input("Correo")
        juego = input("Videojuego favorito: ")
        clientes.append(Cliente(nombre, edad, correo, juego))
    elif opcion == "2":
        if not clientes:
            print("No hay clientes.")
        else:
            for c in clientes:
                c.mostrar()
    
    elif opcion == "3":
        buscar = input("Nombre del videojuego: ").lower()
        encontrados = [c for c in clientes if c.videojuego_favorito.lower() == buscar]
        if not encontrados:
            print("No se encontró ningún cliente")
        else:
            for c in encontrados:
                c.mostrar()
    
    elif opcion == "4":
        break
    
    else:
        print("Opción no válida")