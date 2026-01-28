# Indroduccion brece y contexalizacion
Después de un día intenso de estudio, actividades como jugar videojuegos, ver anime o películas ayudan a relajarse. De forma similar, en programación usamos estructuras de control como if-else para tomar decisiones automáticas según una condición, en este caso, la edad del usuario.






# Desarrollo técnico correcto y preciso

### primero  emiezo la php con la etiqutas
```
<?php

?>
```
### crear variable `edad`

```
$edad_usuario = 47 
```
### crear un structura con la if y else 
```
if ($edad_usuario < 30){
    echo "Eres un joven"
}
else{
    echo "Ya no eres un joven"
}
```
### crear funcion para muestar informacion con valor de cojer 
```
function mostrar_mensaje ($edad,$mensaje)
    if ($edad < 30) {
        echo "Eres un joven";
    } else {
        echo $mensaje;
    }
```
### dentro de este funcion crear una structura if else 

```
    if ($edad < 30) {
        echo "Eres un joven";
    } else {
        echo $mensaje;
    }
```

### llama la funcion y dame unas valor en la ella 
```
mostrar_mensaje($edad_usuario, "Ya no eres un joven");

```


# Codigo completa

```
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


```

# Cierre/Conclusión enlazando con la unidad
Este ejercicio refuerza los conceptos aprendidos en la unidad sobre estructuras condicionales y funciones en PHP.
Aprender a encapsular la lógica dentro de funciones permite crear código más ordenado, reutilizable y fácil de mantener.