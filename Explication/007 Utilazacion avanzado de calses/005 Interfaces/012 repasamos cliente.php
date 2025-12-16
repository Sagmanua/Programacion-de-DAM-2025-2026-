<?php
    $campos_clientes = [
        "nombre",
        "apellidos",
        "email",
        "telefono",
        "direccion"
    ];

    foreach($campos_clientes as $campo){
        echo $campo."<br>";
    }
  
?>