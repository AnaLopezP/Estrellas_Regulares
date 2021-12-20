# Estrellas_Regulares

Mi dirección de GitHub para este repositorio es la siquiente: [GitHub](https://github.com/AnaLopezP/Estrellas_Regulares)
https://github.com/AnaLopezP/Estrellas_Regulares

He creado un programa que dibuja y colorea una estrella dependiendo de como lo quiera el usuario.

El codigo del trabajo es el siguiente:
```**import turtle
from turtle import *
def dibujar_estrella(puntas, color_1, color_2):
    color(color_1, color_2)
    begin_fill()
    puntas_int = int(puntas)
    cociente, resto = divmod(puntas_int, 2)
    if resto == 0:
        puntas_int = puntas_int/2
    angulo = 180 - (180/puntas_int)
    while True:
        forward(200)
        left(angulo)
        if abs(pos()) < 1:
            break
    end_fill()
    done()

print("¿De cuantas puntas quieres tu estrella? Minimo de 5 puntas e impar.")
puntas = input()
print("Y de que dos colores la quieres? En inglés.")
color_1 = input()
color_2 = input()
dibujar_estrella(puntas, color_1, color_2)
```


