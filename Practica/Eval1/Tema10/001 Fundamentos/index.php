<?php
$edad_usuario = 47 

if ($edad_usuario < 30){
    echo "Eres un joven"
}
else{
    echo "Ya no eres un joven"
}

function mostrar_mensaje ($edad,$mensaje)
    if ($edad < 30) {
        echo "Eres un joven";
    } else {
        echo $mensaje;
    }
mostrar_mensaje($edad_usuario, "Ya no eres un joven");


?>

