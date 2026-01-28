# Indroduccion brece y contexalizacion
Para practicar el concepto de jerarquías de clases en JavaScript, el alumno debe crear un nuevo archivo HTML y agregar los siguientes elementos:

En el archivo HTML, crea una estructura básica con un div que contendrá todos tus elementos. Añade un evento de teclado para cambiar la posición del jugador (nave) cada vez que se presiona una tecla.




# Desarrollo técnico correcto y preciso
## index.html
### Despues de crear una gile `index.html` voy a hacer una pagina
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
### Esribo `<body>` que es contiene todo lo que se muestra en la pantalla: encabezado, menú, contenido principal y pie de página y creo la `div`con id 
```
<body>
    <div id="nave"></div>
</body>
```
### Esribo `<script>` que es contiene el JavaSript codigo dentro de etiqutas 
```
let hoy = new Date();
console.log(hoy);
```
### crea una clase para `nave` que contiene `constructor` y `move`
```
    class Nave {
      constructor(x, y) {
        this.posx = x;
        this.posy = y;
      }
      
      move(dx, dy) {
        this.posx += dx;
        this.posy += dy;
      }
    }
```
### Creo una instancia de la nave
```
let nave = new Nave(Math.random()*1000, Math.random()*500);
``` 
### creo una `addEventListener` que cuando user presiona el botón  JS liedo ay llam funcion evento key leido este y probar todo en `swith` si botones corectas llame nave y muevo
``` 
document.addEventListener("keydown", function(event){
    switch(event.key){
        case "w":
            nave.move(0,-5);
            break;
        case "s":
            nave.move(0,5);
            break;
        case "a":
            nave.move(-5,0);
            break;
        case "d":
            nave.move(5,0);
            break;
    }
```
### Creo la posicion de la nave
```
document.querySelector('#nave').style.left = nave.posx + 'px';
document.querySelector('#nave').style.top = nave.posy + 'px';
```

 

# Codigo completa
## index.html
```
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Jerarquías de clases en JavaScript</title>
</head>
<body>
  <div id="nave"></div>
  
  <script>
    // Crea una clase para la nave
    class Nave {
      constructor(x, y) {
        this.posx = x;
        this.posy = y;
      }
      
      move(dx, dy) {
        this.posx += dx;
        this.posy += dy;
      }
    }
    
    // Crea una instancia de la nave
    let nave = new Nave(Math.random()*1000, Math.random()*500);
  
  document.addEventListener("keydown", function(event){
       switch(event.key){
          case "w":
              nave.move(0,-5);
              break;
          case "s":
              nave.move(0,5);
              break;
          case "a":
              nave.move(-5,0);
              break;
          case "d":
              nave.move(5,0);
              break;
        }
      document.querySelector('#nave').style.left = nave.posx + 'px';
      document.querySelector('#nave').style.top = nave.posy + 'px';
  });
  </script>
</body>
</html>
```

# Cierre/Conclusión enlazando con la unidad
En este ejemplo, creamos una clase Nave que tiene un constructor y una propiedad move. La instancia de la clase se crea con el evento de teclado "keydown" para cambiar la posición de la nave. En cada caso, llamamos al método move de la clase Nave para cambiar la posición.