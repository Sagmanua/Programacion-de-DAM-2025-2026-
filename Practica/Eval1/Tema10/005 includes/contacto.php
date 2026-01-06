<?php include 'cabecera.php'; ?>
<h2>Contacto</h2>
<form action="enviar.php" method="POST">
        <label for="nombre">Nombre:</label><br>
        <input type="text" id="nombre" name="nombre" required><br><br>
        
        <label for="email">Correo electrónico:</label><br>
        <input type="email" id="email" name="email" required><br><br>
        
        <label for="mensaje">Mensaje:</label><br>
        <textarea id="mensaje" name="mensaje" rows="4" required></textarea><br><br>
        
        <button type="submit">Enviar mensaje</button>
    </form>
<?php include 'pie.php'; ?>