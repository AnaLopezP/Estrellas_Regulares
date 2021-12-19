import turtle
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

print("¿De cuantas puntas quieres tu estrella? Minimo de 5 puntas e impar. Si pones un numero par saldrá el doble, ya que las puntas pares no se pueden dibujar de una sola trazada.")
puntas = input()
print("Y de que dos colores la quieres?")
color_1 = input()
color_2 = input()
dibujar_estrella(puntas, color_1, color_2)