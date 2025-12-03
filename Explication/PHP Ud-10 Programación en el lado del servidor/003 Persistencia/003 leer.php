<?php
    $archivo = fopen("archivo.txt", "r");
    $contenid = fread($archivo,filesize("archivo.txt")); // "r" = read 
    echo $contenid;
    fclose($archivo);
?>