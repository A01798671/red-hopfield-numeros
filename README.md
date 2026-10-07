# Red Hopfield para reconocimiento de figuras

Este proyecto implementa una red neuronal Hopfield en Python para reconocer y recuperar figuras representadas mediante matrices binarias.

La red utiliza patrones almacenados en archivos `.txt`, los convierte a vectores y construye una matriz de pesos para posteriormente intentar recuperar una figura objetivo aunque tenga modificaciones o ruido.

## Estructura del proyecto

```text
red-hopfield-numeros/
├── main.py
└── dataset/
    ├── uno.txt
    ├── dos.txt
    ├── tres.txt
    └── x.txt