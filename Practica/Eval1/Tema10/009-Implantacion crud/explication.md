# Indroduccion brece y contexalizacion
El manejo de errores en estructuras de datos es esencial para garantizar que los programas funcionen de forma correcta y segura. Cuando una estructura se usa de manera incorrecta —por ejemplo, accediendo a posiciones inválidas o insertando datos erróneos— pueden producirse fallos que afectan al rendimiento, a la integridad de la información o incluso a la estabilidad del sistema. Por ello, comprender y aplicar técnicas adecuadas de control de errores permite desarrollar aplicaciones más robustas, fiables y fáciles de mantener.




# Desarrollo técnico correcto y preciso
## index.php
### al primero crear raiz file para nustro noticias que contiene link a (read) listar todo de los contenido de bases de datos 
```
<?php
include __DIR__ . '/inc/listar_articulos.php';
?>
```
## listar_articulos.php
### hago un coneccion a bases de datos para puede listar todos los objetos
```
$host = "localhost";
$user = "periodico";
$pass = "Periodico123$";
$db   = "periodico";
$conexion = new mysqli($host, $user, $pass, $db);
$sql = "SELECT * FROM noticias";
$resultado = $conexion->query($sql);
``` 
### hace un scipt cuando llame para todos los fila echo este codigo
```
while ($fila = $resultado->fetch_assoc()) {
```
### usa `fetch_assoc` para duevlco una structura de HTML con datos de la bases de datos
```
          echo '
            <article>
              <h3>'.$fila['titulo'].'</h3>
              <time>'.$fila['fecha_publicacion'].'</time>
              <p>'.$fila['autor_id'].'</p>
              <p>'.$fila['contenido'].'</p>
            </article>
          ';
```
## formulario.php
### este codigo hace una `insert` en bases de datos
### al principoi creao una forma que (en mi caso admin) puede añade nuevos registros en bases de datos
```
<form action="formulario.php" method="POST">
	<div class="controlformulario">
    <label for="titulo">Título de la nueva noticia</label>
    <input type="text" name="titulo" id="titulo">
  </div>
  
  <div class="controlformulario">
  	<label for="contenido">Contenido de la nueva noticia</label>
		<textarea id="contenido" name="contenido"></textarea>
  </div>
  
  <div class="controlformulario">
  	<label for="fecha_publicacion">Fecha de la nueva noticia</label>
		<input type="text" name="fecha_publicacion" id="fecha_publicacion">
  </div>
  
  <div class="controlformulario">
  	<label for="autor_id">Autor de la nueva noticia</label>
		<input type="text" name="autor_id" id="autor_id">
  </div>
    
  <input type="submit">
  
</form>
``` 
### en parte php Atrapo el informacion de `titulo` `contenido` `fecha_publicacion` y `autor_id`
```
$titulo = $_POST['titulo'];									
$contenido = $_POST['contenido'];								
$fecha_publicacion = $_POST['fecha_publicacion'];	
$autor_id = $_POST['autor_id'];		
```
### conecta ete file a bases de datos 
```
$host = "localhost";											
$user = "periodico";
$pass = "Periodico123$";
$db   = "periodico";

$conexion = new mysqli($host, $user, $pass, $db);	// Ejecuto la conexion
```
###  Lanzo la peticion de inserts
```
$sql = "
INSERT INTO noticias VALUES(
    NULL,
    '".$titulo."',
    '".$contenido."',
    '".$fecha_publicacion."',
    ".$autor_id."
);
";
```
## Ejecuto la peticion
```
$conexion->query($sql);
```
## Cierro la conexion
```
$conexion->close();
```
## elimenar.php
### este codigo hace una `elimina` en bases de datos
### al principoi creao una forma que (en mi caso admin) puede añade nuevos registros en bases de datos
```
<form action="formulario.php" method="POST">
  
  <div class="controlformulario">
  	<label for="autor_id">Autor de la nueva noticia</label>
		<input type="text" name="autor_id" id="autor_id">
  </div>
    
  <input type="submit">
  
</form>
``` 
### en parte php Atrapo el informacion de y`autor_id`
```
$autor_id = $_POST['autor_id'];		
```
### conecta ete file a bases de datos 
```
$host = "localhost";											
$user = "periodico";
$pass = "Periodico123$";
$db   = "periodico";

$conexion = new mysqli($host, $user, $pass, $db);	// Ejecuto la conexion
```
###  Lanzo la peticion de eliminar
```
  $sql = "DELETE FROM noticias WHERE id = ".$id.";";	// Preparo la peticion
```
## Ejecuto la peticion
```
$conexion->query($sql);
```
## Cierro la conexion
```
$conexion->close();
```






# Codigo completa
Project/
├─ explicacion.md
├─ css/
│  └─ style.css
├─ inc/
│  ├─ create/
│  │  └─ formulario.php
│  ├─ delete/
│  │  └─ elimenar.php
│  └─ listar_articulos.php
└─ index.php
## index.php
```
<?php
include __DIR__ . '/inc/listar_articulos.php';
?>
```
## listar_articulos.php
```
<?php
        $host = "localhost";
        $user = "periodico";
        $pass = "Periodico123$";
        $db   = "periodico";
        $conexion = new mysqli($host, $user, $pass, $db);
        $sql = "SELECT * FROM noticias";
        $resultado = $conexion->query($sql);
        while ($fila = $resultado->fetch_assoc()) {
          echo '
            <article>
              <h3>'.$fila['titulo'].'</h3>
              <time>'.$fila['fecha_publicacion'].'</time>
              <p>'.$fila['autor_id'].'</p>
              <p>'.$fila['contenido'].'</p>
            </article>
          ';
        }
        $conexion->close();
      ?>
```
## formulario.php
```
<form action="formulario.php" method="POST">
	<div class="controlformulario">
    <label for="titulo">Título de la nueva noticia</label>
    <input type="text" name="titulo" id="titulo">
  </div>
  
  <div class="controlformulario">
  	<label for="contenido">Contenido de la nueva noticia</label>
		<textarea id="contenido" name="contenido"></textarea>
  </div>
  
  <div class="controlformulario">
  	<label for="fecha_publicacion">Fecha de la nueva noticia</label>
		<input type="text" name="fecha_publicacion" id="fecha_publicacion">
  </div>
  
  <div class="controlformulario">
  	<label for="autor_id">Autor de la nueva noticia</label>
		<input type="text" name="autor_id" id="autor_id">
  </div>
  
  <input type="submit">
  
</form>
<?php

  $titulo = $_POST['titulo'];									
  $contenido = $_POST['contenido'];								
  $fecha_publicacion = $_POST['fecha_publicacion'];	
  $autor_id = $_POST['autor_id'];								

  $host = "localhost";											
  $user = "periodico";
  $pass = "Periodico123$";
  $db   = "periodico";

  $conexion = new mysqli($host, $user, $pass, $db);	// Ejecuto la conexion

  $sql = "
  	INSERT INTO noticias VALUES(
    	NULL,
      '".$titulo."',
      '".$contenido."',
      '".$fecha_publicacion."',
     	".$autor_id."
    );
  ";																								
  $conexion->query($sql);
	
  $conexion->close();																// Cierro la conexion
  header("Location: ../../escritorio.php");												// Y me vuelvo al escritorio
  
?>
```
## elimenar.php
``` 
<form action="eliminar.php" method="POST">
	<div class="controlformulario">
    <label for="titulo">Título de la nueva noticia</label>
    <input type="text" name="titulo" id="titulo">
  </div>
  
  <div class="controlformulario">
  	<label for="contenido">Contenido de la nueva noticia</label>
		<textarea id="contenido" name="contenido"></textarea>
  </div>
  
  <div class="controlformulario">
  	<label for="fecha_publicacion">Fecha de la nueva noticia</label>
		<input type="text" name="fecha_publicacion" id="fecha_publicacion">
  </div>
  
  <div class="controlformulario">
  	<label for="autor_id">Autor de la nueva noticia</label>
		<input type="text" name="autor_id" id="autor_id">
  </div>
  
  <input type="submit">
  
</form>
<?php

  $id = $_GET['id'];											
  $host = "localhost";											
  $user = "periodico";
  $pass = "Periodico123$";
  $db   = "periodico";

  $conexion = new mysqli($host, $user, $pass, $db);	// Ejecuto la conexion

  $sql = "DELETE FROM noticias WHERE id = ".$id.";";	// Preparo la peticion																							
  $conexion->query($sql);														
	
  $conexion->close();										
  header("Location: escritorio.php");					
  
?>
```

# Cierre/Conclusión enlazando con la unidad
Este ejercicio permite comprender de manera práctica cómo las estructuras de almacenamiento organizan y gestionan diferentes tipos de datos dentro de un sistema. Al trabajar con noticias —cada una compuesta por campos como título, contenido, fecha o identificadores— se evidencia la importancia de elegir estructuras adecuadas y aplicarlas correctamente para insertar, listar o eliminar información. Además, el proceso muestra cómo el manejo de errores es esencial para evitar inconsistencias y asegurar que las operaciones sobre los datos se realicen de forma segura y controlada. En conjunto, la actividad refuerza los conceptos de la unidad, demostrando cómo los principios teóricos sobre estructuras de datos se aplican directamente en el desarrollo de aplicaciones funcionales.