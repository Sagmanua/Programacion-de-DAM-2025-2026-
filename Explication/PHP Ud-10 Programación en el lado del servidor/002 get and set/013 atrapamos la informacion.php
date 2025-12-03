<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="012-style.css">
    </head>
    <body>
    <header>
        <h1>Preguntas y respuestas </h1>
        


    </header>
    <main>
        <form>
            <form action='?' method="POST">
            <label for="pregunta">Introduce la pregunta</label>
            <input type="text" name="pregunta" id="pregunta">
            <label for="respuesta">Introduce la respuesta</label>
            <input type="text" name="respuesta" id="respuesta">
            <input type="submit">

    </main>
    <footer>
    	(c) 2025 Bohdan Sydorenko
        <?php
            echo $_POST['pregunta'];
            echo "<br>";
            echo $_POST['respuesta'];
        ?>
    </footer>

</html>