<html>
<body>

<form method="post" action="indexparte4.php">
    Pregunta:   <input type="text" name="Pregunta">
    Respuesta:  <input type="text" name="Respuesta">
    <input type="submit">
</form>

</body>
</html>
<?php
$pregunta = htmlspecialchars($_POST['Pregunta']);
$respuesta = htmlspecialchars($_POST['Respuesta']);
echo $pregunta;
echo $respuesta;
$json_pregunta =  json_encode($pregunta);
$json_respuesta =  json_encode($respuesta);
echo $json_pregunta;
echo $json_respuesta;
