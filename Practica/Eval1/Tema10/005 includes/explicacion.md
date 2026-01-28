# Indroduccion brece y contexalizacion
 En nuestra clase de programación, hemos estado trabajando en bloques y estructuras fundamentales para crear páginas web dinámicas utilizando PHP. Hoy, vamos a integrar estos conocimientos con un proyecto sencillo que te permitirá practicar cómo incluir bloques reutilizables en tus páginas web.




# Desarrollo técnico correcto y preciso
## para empezar crear php voy a crear cabecera.php y pie.php usa esta porque voy a usar en la cada pagina de mi proyecto.Detro de estos file esta html structura y navigacion panel
### cabecera.php
#### esta empezar la delacracion de la HTML y navigacion 
##### declara html format
```
<!doctype html>
<html lang="es">
```

##### creao `head`
```
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="style.css?v=2">
    <title>Recipe App</title>
</head>
```
##### creao navigacion panel `nav` con pequeño
```
<nav>
    <ul>
        <li><a href="index.php">Inicio</a></li>
        <li><a href="sobremi.php">Sobre mí</a></li>
        <li><a href="contacto.php">Contacto</a></li>
    </ul>
</nav>
```
##### y empezar `main`
```
<main>
```


### pie.php
#### ciero la `main` 
```
</main>
```
#### tengo `footer` pero no usa 
```
<footer>
</footer>
```
#### ciero la `body` 
```
</body>
```
#### ciero la `html` 
```
</html>
```

## index.php
### include file `cabecera.php` al principio de la file y include `pie.php` al final de file 
```
<?php include 'cabecera.php'; ?>
----contenido
<?php include 'pie.php'; ?>
```
### en la contenido hace pequiño describe de esta pagin con imagen. Uso `h2` `p` y `img`
```
<h2>Bienvenido a mi sitio web</h2>
<p>Esta es la página principal. Aquí puedes encontrar las últimas novedades y proyectos en los que he estado trabajando.</p>
<img src="banner.jpg" alt="Imagen de bienvenida" style="width:100%; max-width:600px;">
```
## sobremi.php
### include file `cabecera.php` al principio de la file y include `pie.php` al final de file 
```
<?php include 'cabecera.php'; ?>
----contenido
<?php include 'pie.php'; ?>
```
### en la contenido hace pequiño describe de esta pagin co una lista. Uso `h2` `h3` `p` `ul` `li`
```
<?php include 'cabecera.php'; ?>

    <h2>Sobre mí</h2>
    <p>Hola, soy Bohdan. Me apasiona el desarrollo web y la creación de soluciones digitales eficientes.</p>
    <h3>Mi experiencia</h3>
    <ul>
        <li>Desarrollo Frontend (HTML, CSS, JS)</li>
        <li>Programación Backend (PHP, MySQL)</li>
    </ul>

<?php include 'pie.php'; ?>
```

## contacto.php
### include file `cabecera.php` al principio de la file y include `pie.php` al final de file 
```
<?php include 'cabecera.php'; ?>
----contenido
<?php include 'pie.php'; ?>
```
### en la contenido hace pequiño describe de esta pagin co una lista. Uso `h2` `p`
<h2>Contacto</h2>
<p>Aqui solo pongo el contenido de la pagina de contacto</p>



# Codigo completa
Project/
├─ explicacion.md
├─ contacto.php
├─ cabecera.php
├─ pie.php
├─ sobremi.php
└─ index.php
## contacto.php
```
<?php include 'cabecera.php'; ?>
<h2>Contacto</h2>
<p>Aqui solo pongo el contenido de la pagina de contacto</p>
<?php include 'pie.php'; ?>
```
## cabecera.php
```
<!doctype html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="style.css?v=2">
    <title>Recipe App</title>
</head>
<nav>
    <ul>
        <li><a href="index.php">Inicio</a></li>
        <li><a href="sobremi.php">Sobre mí</a></li>
        <li><a href="contacto.php">Contacto</a></li>
    </ul>
</nav>
    <main>
```
## pie.php
```
		</main>
  	<footer>
    </footer>
  </body>
</html>
```
## sobremi.php
```
<?php include 'cabecera.php'; ?>

    <h2>Sobre mí</h2>
    <p>Hola, soy Bohdan. Me apasiona el desarrollo web y la creación de soluciones digitales eficientes.</p>
    <h3>Mi experiencia</h3>
    <ul>
        <li>Desarrollo Frontend (HTML, CSS, JS)</li>
        <li>Programación Backend (PHP, MySQL)</li>
    </ul>

<?php include 'pie.php'; ?>
```
## index.php
```
<?php include 'cabecera.php'; ?>

    <h2>Bienvenido a mi sitio web</h2>
    <p>Esta es la página principal. Aquí puedes encontrar las últimas novedades y proyectos en los que he estado trabajando.</p>
    <img src="banner.jpg" alt="Imagen de bienvenida" style="width:100%; max-width:600px;">

<?php include 'pie.php'; ?>
```
# Cierre/Conclusión enlazando con la unidad
Este ejercicio demuestra cómo el uso de bloques reutilizables en PHP simplifica el desarrollo de sitios web y mejora la organización del código. Al centralizar elementos comunes, cualquier cambio en el diseño o estructura puede realizarse de forma rápida y eficaz, afectando a todas las páginas al mismo tiempo.