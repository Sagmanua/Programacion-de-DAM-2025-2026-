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
    header("Location: escritorio.php");					// Y me vuelvo al escritorio
  
?>