<?php
    session_start();

    if (!isset($_SESSION['idioma'])) {
        $_SESSION['idioma'] = 'es';
    }

    if (isset($_GET['idioma'])) {
        $_SESSION['idioma'] = $_GET['idioma'];
    }

    $idioma['es']['inicio'] = "Inicio";
    $idioma['es']['sobremi'] = "Sobre mi";
    $idioma['es']['proyectos'] = "Proyectos";
    $idioma['es']['contacto'] = "Contacto";

    $idioma['en']['inicio'] = "Home";
    $idioma['en']['sobremi'] = "About me";
    $idioma['en']['proyectos'] = "Projects";
    $idioma['en']['contacto'] = "Contact";
?>
<!doctype html>
<html lang="es">
<head>
    <title>Multi idioma</title>
    <meta charset="utf-8">
</head>
<body>
    <select>
    <option value="es">🇪🇸</option>
    <option value="en">🇬🇧</option>
    </select>
    <h1>Jose Vicente Carratala</h1>
    <nav>
    <a href=""><?= $idioma[$_SESSION['idioma']]['inicio'] ?></a>
    <a href=""><?= $idioma[$_SESSION['idioma']]['sobremi'] ?></a>
    <a href=""><?= $idioma[$_SESSION['idioma']]['proyectos'] ?></a>
    <a href=""><?= $idioma[$_SESSION['idioma']]['contacto'] ?></a>
    </nav>
</body>
</html>