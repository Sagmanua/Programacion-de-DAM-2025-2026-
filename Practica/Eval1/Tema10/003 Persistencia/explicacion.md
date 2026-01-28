# Indroduccion brece y contexalizacion

En nuestra clase hemos estado explorando cómo almacenar y manipular datos en PHP utilizando arrays nombrados y JSON. Estos conceptos son fundamentales para el manejo de información en aplicaciones web. Además, como aficionado a los videojuegos y las series anime, te propongo una actividad que combina estos conocimientos con tus pasatiempos favoritos.

# Desarrollo técnico correcto y preciso
## index.php
### parte 1-3  
#### declara la php
```
<?php
?>
```
#### crear array de `clientes`
```
$cliente = array();
``` 

#### pasa valores en la array que creado antes
```
$cliente['nombre'] = "Jose Vicente";
$cliente['apellidos'] = "Carratalá";
$cliente['email'] = "jose@ejemplo.com";
```
#### muestro en la pantalla array de los datos
```
echo "El cliente es: " . $cliente['nombre'] . " " . $cliente['apellidos'];
```

#### crear variable `json` que encode array en la json array y imprime en la pantalla 

```
$json =  json_encode($cliente);
echo $json;
```


## indexparte4.php
### Crear structura de la html facil 
```
<html>
    <body>
    </body>
</html>
```
### ahora crear una `form` dentor declara php file par enviar. Dentro de la `form` crear 2 `input` una para escribir texto y ontra para enviar la enla index php
```
<form method="post" action="indexparte4.php">
    Pregunta:   <input type="text" name="Pregunta">
    Respuesta:  <input type="text" name="Respuesta">
    <input type="submit">
</form>
```

### declara la php
```
<?php
?>
```

### hace metodo post que debe cojer informacion gue inviado de `indexparte4.php` y procesa
```
$pregunta = htmlspecialchars($_POST['Pregunta']);
$respuesta = htmlspecialchars($_POST['Respuesta']);
```

### y demuestra este mensaje de la web 
```
echo $pregunta;
echo $respuesta;
```
#### crear variable `json` que encode array en la json array y imprime en la pantalla 

```
$json_pregunta =  json_encode($pregunta);
$json_respuesta =  json_encode($respuesta);
echo $json_pregunta;
echo $json_respuesta;

```


# Codigo completa
Project/
├─ explicacion.md
├─ indexparte4.php
└─ index.php
## index.php 
### parte 1-3  
```
<?php
$cliente = array();

$cliente['nombre'] = "Jose Vicente";
$cliente['apellidos'] = "Carratalá";
$cliente['email'] = "jose@ejemplo.com";

echo "El cliente es: " . $cliente['nombre'] . " " . $cliente['apellidos'];

$json =  json_encode($cliente);
echo $json;
```
## indexparte4.php
```
<html>
<body>

<form method="post" action="indexparte4.php">
    Pregunta:   <input type="text" name="Pregunta">
    Respuesta:  <input type="text" name="Respuesta">
    <input type="submit">
</form>

</body>
</html>
<?php
$pregunta = htmlspecialchars($_POST['Pregunta']);
$respuesta = htmlspecialchars($_POST['Respuesta']);
echo $pregunta;
echo $respuesta;
$json_pregunta =  json_encode($pregunta);
$json_respuesta =  json_encode($respuesta);
echo $json_pregunta;
echo $json_respuesta;


```

# Cierre/Conclusión enlazando con la unidad
Estos conocimientos son fundamentales en proyectos reales, ya que el formato JSON se utiliza habitualmente para enviar información entre páginas, formularios, APIs y bases de datos. Dominar estas técnicas permitirá desarrollar aplicaciones web más dinámicas y estructuradas en futuras unidades