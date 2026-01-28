<form action="" method="POST">
<?php
      // PRIMERO CREO LAS CABECERAS //////////////////
        $resultado = $conexion->query("
          SELECT * FROM ".$_GET['tabla']." LIMIT 1;
        ");	// SOLO QUIERO UN ELEMENTO !!!!!!!!!!!!!!!!
        while ($fila = $resultado->fetch_assoc()) {
          foreach($fila as $clave=>$valor){
            echo "<input 
            	type='text' 
              name='".$clave."'
              placeholder='".$clave."'>";
          }
         }
      ?>
</form>
<style>
    form{
        width: 100%;
        display:flex;
        flex-direction:column;
        gap:20px;
    }
    .control_formulario{
  	display:flex;
    }
    label{
        flex:1;
    }
    input{
        flex:4;
        padding:10px;
        border:2px solid plum;
    }

</style>