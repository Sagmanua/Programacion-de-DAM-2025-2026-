<!doctype html>
<html>
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="006-style.css">
    <title>Preguntas y Respuestas</title>
</head>
<body>
<header>
    <h1>Preguntas y respuestas</h1>
</header>

<main>
    <form action="?" method="POST">
        <label for="pregunta">Introduce la pregunta</label>
        <input type="text" name="pregunta" id="pregunta">

        <label for="respuesta">Introduce la respuesta</label>
        <input type="text" name="respuesta" id="respuesta">

        <input type="submit" value="Enviar">
    </form>
</main>

<footer>
    <p>(c) 2025 Bohdan Sydorenko</p>

    <?php
        $json = json_encode($_POST);
        echo $json
    ?>
</footer>
</body>
</html>
