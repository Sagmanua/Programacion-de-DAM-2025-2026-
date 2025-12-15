<?php include "inc/cabecera.php"; ?>

Hola que tal yo soy el carrito<br>
Vamos a ver si atrapamos correctamente el producto<br>
<?php
	echo "El producto es: ".$_POST['id']."<br>";
    echo "Las unidades son: ".$_POST['unidades']."<br>";
?>

<form method="POST" action="finalizar.php">
    <input typy="hidden" name="idproducto" calue="<? $_POST['id']?>">
    <input type="hidden" name="unidades" value="<?= $_POST['unidades'] ?>">

    <input type="text" name="nombre_cliente">
    <input type="text" name="apellidos">
    <input type="text" name="email">
    <input type="text" name="direccion">
    <input type="text" name="telefono">

    <input type="submit">

<?php include "inc/piedepagina.php"; ?>



