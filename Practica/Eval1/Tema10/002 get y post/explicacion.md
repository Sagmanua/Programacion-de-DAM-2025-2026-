# Indroduccion brece y contexalizacion

En nuestro mundo digital actual, las interacciones con aplicaciones web son cada vez más comunes. Para manejar estas interacciones, conocemos los verbos HTTP como GET y POST. El GET se utiliza para solicitar información desde un servidor, mientras que el POST se usa para enviar datos al servidor para su procesamiento.




# Desarrollo técnico correcto y preciso
## index.html
```
<html>
<body>

<form method="post" action="index.php">
  Name: <input type="text" name="fname">
  <input type="submit">
</form>

</body>
</html>
```
### Crear structura de la html facil 
```
<html>
    <body>
    </body>
</html>
```
### ahora crear una `form` dentor declara php file par enviar. Dentro de la `form` crear 2 `input` una para escribir texto y ontra para enviar la enla index php
```
<form method="post" action="index.php">
  Name: <input type="text" name="fname">
  <input type="submit">
</form>
```

## index.php
```
<?php
$name = htmlspecialchars($_POST['fname']);
echo $name;
```
### declara la php
```
<?php
?>
```

### hace metodo post que debe cojer informacion gue inviado de `index.php` y procesa
```
$name = htmlspecialchars($_POST['fname']);
```

### y demuestra este mensaje de la web 
```
echo $name;
```

# Codigo completa
Project/
├─ explicacion.md
├─ index.html
└─ index.php
## index.php
```
<?php
$name = htmlspecialchars($_POST['fname']);
echo $name;
```
## index.html
```
<html>
<body>

<form method="post" action="index.php">
  Name: <input type="text" name="fname">
  <input type="submit">
</form>

</body>
</html>
```

# Cierre/Conclusión enlazando con la unidad


Como aficionado a los videojuegos y series anime, imagina que estás creando una página web donde otros jugadores puedan compartir sus juegos favoritos y animes recientes. Para ello, necesitarás utilizar tanto GET como POST para permitir la interacción con tu sitio web de manera eficiente.