# python 2

# You can edit this code and run it right here in the browser!
# Try changing colors or adding your own shapes.
#no finished

from turtle import *
from math import *
import turtle

def volumen_esfera (radio):
	volumen=4.0/3.0 * pi * radio **3
	return volumen
	
def area_triangulo(base, altura):
	area = 1.0/2.0 * base * altura
	return area
	
def perimetro_circulo (radio):
	perimetro = 2* pi * radio
	return perimetro
	
	
	
def draw_circle(turtle, color, size, x, y):
    penup()
    color(color)
    fillcolor(color)
    goto(x,y)
    pendown()
    begin_fill()
    circle(size)
    end_fill()

	
tommy = turtle.Turtle()
tommy.shape("circle")
tommy.speed(500)

draw_circle(tommy, "green", 50, 25, 0)
draw_circle(tommy, "blue", 50, 0, 0)
draw_circle(tommy, "yellow", 50, -25, 0)


tommy.penup()
tommy.goto(0,-50)
tommy.color("black")
tommy.write("Teach With Code!", None, "center", "16pt bold")
tommy.goto(0,-80)


