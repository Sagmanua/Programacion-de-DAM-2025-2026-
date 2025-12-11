<!-- IMPORTANTE: Este es el index de admin -->
<!doctype html>
<html lang="es">
	<head>
  	<title>El jocarsa - Noticias tecnológicas</title>
    <meta charset="utf-8">
    <style>
        body,html{width:100%;height:100%;padding:0px;margin:0px;background:seagreen;}
        body{display:flex;justify-content:center;align-items:center;}
        form{
      	display:flex;flex-direction:column;gap:20px;
      	padding:20px;background:white;justify-content:center;
        align-items:center;width:200px;height:200px;
        form input{width:100%;padding:10px;box-sizing:border-box;}
        }
    </style>
  </head>
  <body>
  	<form action="procesalogin.php" method="POST">
    	<input type="text" name="usuario" placeholder="usario">
        <input type="text" name="contrasena" placeholder="contrasena">
        <input type="submit">

      
    </form>
  </body>
</html>
