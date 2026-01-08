# Indroduccion brece y contexalizacion
El objetivo de este ejercicio es utilizar los conocimientos adquiridos sobre transformaciones y rotaciones en un ejemplo práctico y visual utilizando HTML, CSS y JavaScript.

Comenzamos con una página web que muestra el reloj del sol. Este reloj se compone de círculos superpuestos que representan las manecillas de las horas, los minutos y los segundos. El objetivo es que nuestro personaje se mueva hacia arriba cuando la tecla "W" se presione, hacia abajo cuando se presione la tecla "S", hacia la izquierda cuando se presione la tecla "A" y hacia la derecha cuando se presione la tecla "D




# Desarrollo técnico correcto y preciso
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
### CSS
#### `width` Define el ancho de un elemento.
#### `border` agrega un borde alrededor del elemento.
#### `position` define cómo se coloca un elemento en la página (relative, absolute, fixed, sticky).
### `overflow` controla qué pasa con el contenido que se sale del área del elemento (visible, hidden, scroll, auto).
### `transition` crea animaciones suaves cuando cambian propiedades CSS (como color, width o height).


```
#escenario{
    width: 400px; height: 
    400px; border: 2px solid black; 
    position: relative; 
    overflow: hidden;
}
#personaje{
    width: 50px; 
    height: 50px; 
    background-color: orange; 
    position: absolute; 
    top: 175px; 
    left: 175px; 
    transition: all 0.2s;

}
#box{
   width: 100%; 
   height: 10px; 
   background-color: black;
}
```
## JS
```
let posX = 175;
let posY = 175;
const personaje = document.getElementById("personaje");
```
### Obtenemos la tecla presionada convertida a mayúscula para evitar errores WASD es bottones de control , si se presiona otra tecla, no hacemos nada
* W Hacia arriba Aplicamos rotación de 0 grados (mirando arriba)
* S Hacia abajo Aplicamos rotación de 180 grados
* A Hacia la izquierda Aplicamos rotación de 270 grados
* D Hacia la derecha Aplicamos rotación de 90 grados
###  Aplicar los cambios de posición finales
    personaje.style.top = posY + "px";
    personaje.style.left = posX + "px";


```
let tecla = evento.key.toUpperCase();
```
### crear `switch`
```
 switch (tecla) {
        case "W": 
            posY -= 10;
            personaje.style.transform = "rotate(0deg)";
            break;
            
        case "S": // Hacia abajo
            posY += 10;
            // Aplicamos rotación de 180 grados
            personaje.style.transform = "rotate(180deg)";
            break;
            
        case "A": // Hacia la izquierda
            posX -= 10;
            // Aplicamos rotación de 270 grados
            personaje.style.transform = "rotate(270deg)";
            break;
            
        case "D": // Hacia la derecha
            posX += 10;
            // Aplicamos rotación de 90 grados
            personaje.style.transform = "rotate(90deg)";
            break;
            
        default:
            return;
    }
```
### Variables para rastrear la posición actual
```
personaje.style.top = posY + "px";
personaje.style.left = posX + "px";
```
# Codigo completa`
## index.html
``` 
<!DOCTYPE html>
<head>

<style>
#escenario{
    width: 400px; height: 
    400px; border: 2px solid black; 
    position: relative; 
    overflow: hidden;
}
#personaje{
    width: 50px; 
    height: 50px; 
    background-color: orange; 
    position: absolute; 
    top: 175px; 
    left: 175px; 
    transition: all 0.2s;

}
#box{
   width: 100%; 
   height: 10px; 
   background-color: black;
}
</style>
</head>
<body>


<div id="escenario" >
    <div id="personaje" >
        <div id="box" ></div>
    </div>
</div>
<script>

let posX = 175;
let posY = 175;
const personaje = document.getElementById("personaje");

window.onkeydown = function(evento) {
    let tecla = evento.key.toUpperCase();

    switch (tecla) {
        case "W": 
            posY -= 10;
            personaje.style.transform = "rotate(0deg)";
            break;
            
        case "S": 
            posY += 10;
            
            personaje.style.transform = "rotate(180deg)";
            break;
            
        case "A": 
            posX -= 10;
            
            personaje.style.transform = "rotate(270deg)";
            break;
            
        case "D": 
            posX += 10;
            personaje.style.transform = "rotate(90deg)";
            break;
            
        default:
            return;
    }

    personaje.style.top = posY + "px";
    personaje.style.left = posX + "px";
};
</script>
</body>
</html>
```
# Cierre/Conclusión enlazando con la unidad
El objetivo de este ejercicio es practicar nuestra comprensión del concepto de transformaciones y rotaciones en un contexto más práctico y visual. Estamos trabajando con un ejemplo específico que debe ajustarse estrictamente al contexto proporcionado, evitando introducir conocimientos externos o temas no permitidos.