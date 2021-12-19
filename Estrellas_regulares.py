import turtle
from turtle import *
def dibujar_estrella(puntas, color_1, color_2):
    color(color_1, color_2)
    begin_fill()
    angulo = 180 - (180/int(puntas))
    print(angulo)
    while True:
        forward(200)
        left(angulo)
        if abs(pos()) < 1:
            break
    end_fill()
    done()

print("¿De cuantas puntas quieres tu estrella? Minimo de 5 puntas.")
puntas = input()
print("Y de que dos colores la quieres?")
color_1 = input()
color_2 = input()
dibujar_estrella(puntas, color_1, color_2)