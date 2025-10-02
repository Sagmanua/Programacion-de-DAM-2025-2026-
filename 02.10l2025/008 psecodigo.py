'''
    Aplicacion de gestion de produsctos
    (c) 2025 Bohdan Sydorenko
    Esta aplicacion gestiona productos

'''

#En este aplicaion no aplica de importa variable 

opcion = None


class Producto():
    def __init__(self):
        self.nombre = None
        self.precio = None
# Creamos las variables globales 

productos = []

# Primero lanzamos in mensage de bienvenda 
print("gestoe de prodictos  v0.l Bohdan Sydorenko")
while True:
    # Mpsramos al usario las opcion que tiene
    print("Selecciona una nuevo opcion" \
    "\n1.-Crear una opcion:" \
    "\n2.-listar productos" \
    "\n3.-Actulizar protucdos" \
    "\n4.-eliminae productos" )
    # En funcion de la opcopn que coja el usario
    # 0 Bien creamos un nuevo priductos 

    if opcion ==1:
        print("creamos un nuevo productos")

    # vien listamos los productos 

    elif opcion == 2:
        print("Vamos a listar los productos")
    #bien actulizamos los productos

    elif opcion == 3:
        print("Vamos a atuliazr productos")

    # vien eliminosmos los producros
    elif opcion == 4:
        print("Vamos a eliaminar prosuctos")
    break
    # y volmemos a repetir
