<?php
    $sql = "INSERT INTO ".$_GET['tabla']." VALUES (";	
foreach($_POST as $clave=>$valor){							
    if($clave == "id"){														
        $sql.= "NULL,";															
    }else{																				
        $sql.= "'".$valor."',";											
    }
}

$sql = substr($sql, 0, -1); 
$sql .= ");";
echo $sql;

$resultado = $conexion->query($sql);						// Proceso el SQL
header("Location: ?tabla=".$_GET['tabla']);																			
?>