# Clase05 — Calculadora estática


## Estructura
Clase05/ │ index.html │ estilos.css │ selectors.md └─ README.md
## Cómo abrir
1. Copia los archivos en una carpeta llamada `Clase05`.
2. Abre `index.html` en tu navegador (doble clic o arrastrar al navegador).


## Verificación rápida con DevTools
- Abre DevTools (F12 o clic derecho → Inspeccionar).
- En la pestaña **Elements**, busca y selecciona los elementos por su id.
- Prueba los selectores en la consola. Ejemplos:


```js
// pinta un borde rojo en el input num1
document.querySelector('#num1').style.border = '2px solid red';


// selecciona el radio de sumar
document.querySelector('input[name="operacion"][value="sumar"]').checked = true;


// dispara submit (si querés ver el comportamiento estático)
document.querySelector('#form-calculadora').submit();