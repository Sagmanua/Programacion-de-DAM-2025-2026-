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

  $id = $_GET['id'];																// Atrapo el id a eliminar

  $host = "localhost";															// Me conecto a la base de datos
  $user = "periodico";
  $pass = "Periodico123$";
  $db   = "periodico";

  $conexion = new mysqli($host, $user, $pass, $db);	// Ejecuto la conexion

  $sql = "DELETE FROM noticias WHERE id = ".$id.";";	// Preparo la peticion																							// Lanzo la peticion de insert
  $conexion->query($sql);														// Ejecuto la peticion
	
  $conexion->close();																// Cierro la conexion
  header("Location: escritorio.php");					// Y me vuelvo al escritorio
  
?>