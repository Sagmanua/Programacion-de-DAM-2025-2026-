# Indroduccion brece y contexalizacion
Durante el tiempo libre, disfruto mucho jugando videojuegos y viendo series anime. Crear este panel de control me ayudará a mantener un seguimiento de mis actividades diarias, como jugar videojuegos o ver películas.




# Desarrollo técnico correcto y preciso
## navegacion.php
### Crea un archivo llamado `navegacion.php` en la carpeta `bloques`.
#### Dentro del archivo, crea una lista desordenada `<ul>` con enlaces  `<a>` que representen diferentes opciones de navegación. Por ejemplo: `Inicio`, `Historial de actividades`, `Contacto`.
```
<ul>
    <li><a href="index.php">Inicio</a></li>
    <li><a href="historial.php">Historial de actividades</a></li>
    <li><a href="contacto.php">Contacto</a></li>
</ul>
``` 
## tabla.php
### Crea un archivo llamado `tabla.php` en la carpeta `bloques`.
#### Dentro del archivo, crea una tabla con cuatro columnas `<th>`: `Nombre`, `Apellidos`, `Email` y `Dirección`. 
```
<table>
    <thead>
        <tr>
            <th>Nombre</th>
            <th>Apellidos</th>
            <th>Email</th>
            <th>Dirección</th>
        </tr>
    </thead>
</table>
```
#### Añade tres filas `<tr>` con datos de ejemplo para mostrar cómo se verá la tabla.
```
<tbody>
    <tr>
        <td>Ana</td>
        <td>García Pérez</td>
        <td>ana.garcia@email.com</td>
        <td>Calle Mayor 12, Madrid</td>
    </tr>
    <tr>
        <td>Juan</td>
        <td>López Martínez</td>
        <td>juan.lopez@email.com</td>
        <td>Avenida del Sol 45, Barcelona</td>
    </tr>
    <tr>
        <td>María</td>
        <td>Rodríguez Ruiz</td>
        <td>m.rodriguez@email.com</td>
        <td>Plaza de la Luna 3, Sevilla</td>
    </tr>
</tbody>
``` 

### Crea un archivo llamado `paneldecontrol.php` en la raiz.
####  En la sección <nav>, incluye el archivo navegacion.php usando la etiqueta 
```
<?php include "bloques/navegacion.php" ?>
```

#### En la sección <main>, incluye el archivo tabla.php usando la etiqueta 
```
<?php include "bloques/tabla.php" ?>.
```
# Codigo completa
Project/
├─ explicacion.md
├─ bloques
    ├─ navegacion.php
    └─ tabla.php
└─ paneldecontrol.php
## navegacion.php
```
<ul>
    <li><a href="index.php">Inicio</a></li>
    <li><a href="historial.php">Historial de actividades</a></li>
    <li><a href="contacto.php">Contacto</a></li>
</ul>
```
## tabla.php
```
<table>
    <thead>
        <tr>
            <th>Nombre</th>
            <th>Apellidos</th>
            <th>Email</th>
            <th>Dirección</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ana</td>
            <td>García Pérez</td>
            <td>ana.garcia@email.com</td>
            <td>Calle Mayor 12, Madrid</td>
        </tr>
        <tr>
            <td>Juan</td>
            <td>López Martínez</td>
            <td>juan.lopez@email.com</td>
            <td>Avenida del Sol 45, Barcelona</td>
        </tr>
        <tr>
            <td>María</td>
            <td>Rodríguez Ruiz</td>
            <td>m.rodriguez@email.com</td>
            <td>Plaza de la Luna 3, Sevilla</td>
        </tr>
    </tbody>
</table>

    
```
## paneldecontrol.php
```
<nav>
    <?php include 'bloques/navegacion.php'; ?>
<nav>
<main>
    <?php include "bloques/tabla.php" ?>
<main>
```

# Cierre/Conclusión enlazando con la unidad
En este proyecto he aplicado los conocimientos aprendidos sobre estructura de páginas web con php y la inclusión de archivos con PHP para construir un panel de control funcional. A través de la creación de bloques separados para la navegación y la tabla de usuarios, aprendí a organizar el código de manera modular, lo que facilita su mantenimiento y reutilización en futuros proyectos.