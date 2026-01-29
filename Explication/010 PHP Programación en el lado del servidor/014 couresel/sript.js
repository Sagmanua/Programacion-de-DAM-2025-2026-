let contenedor = document.querySelector(".jocarsacarrusel");
let contenido = document.querySelectorAll(".jocarsacarrusel img")
contenido.forEach(function(elemento){
    elemento.remove()
})
let nuevo_contenedor = document.createElement("section")
nuevo_contenedor.style.left = 0
contenedor.appendChild(nuevo_contenedor)

contenido.forEach(function(elemento){
    nuevo_contenedor.appendChild(elemento)
})
let botonatras = document.createElement("button")
botonatras.textContent = "◀"
contenedor.appendChild(botonatras)
let botondelante = document.createElement("button")
botondelante.textContent = "▶"
contenedor.appendChild(botondelante)
var anchura = 1280;
var contador = 0;
botondelante.onclick = function(){
    contador--;
    nuevo_contenedor.style.left = contador*anchura+"px"
}
botonatras.onclick = function(){
    contador++;
    nuevo_contenedor.style.left = contador*anchura+"px"
}
