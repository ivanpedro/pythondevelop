from turtle import *
from math import *
from random import *
import turtle

# 'a =%d y b = %d' % (a,b) sustitucion en cadena

#Start Spiral
def colorear():
	c =  ['green','red','blue','yellow','orange',
	'purple','brown','pink','violet','lightblue',
	'lightpink','lightgreen','lime', '#28e078', '#afc8f9']
	return choice(c)

def volumen_esfera (radio):
	volumen=4.0/3.0 * pi * radio **3
	return volumen
	
def area_triangulo(base, altura):
	area = 1.0/2.0 * base * altura
	return area
	
def perimetro_circulo (radio):
	perimetro = 2* pi * radio
	return perimetro
	
def triangulo(value):
		Pencil = turtle.Turtle ()
		Pencil.speed (0)
		Pencil.color (colorear())
		Pencil.penup()
		# position of the cursor at the bottom right 
		Pencil.goto(-250,-250) 
		Pencil.pendown()
		for i in range (1,250):
			Pencil.forward(value)
			Pencil.left(120)
			value = value - 2
		


def cuadrado(value):
		Pencil = turtle.Turtle ()
		Pencil.speed (0)
		Pencil.color (colorear())
		
		Pencil.penup()
		# position of the cursor at the bottom right 
		Pencil.goto(0,0) 
		Pencil.pendown()
		for i in range (1,250):
			value = value + 2 
			Pencil.forward(value)
			Pencil.right(92)
			   
def circulo(turtle, color, size, x ,y):
	Pencil=turtle.Turtle()
	Pencil.speed(500)
	#Pencil.shape("turtle")
	Pencil.color(color)
	Pencil.fillcolor(color)
	Pencil.goto(x,y)
	Pencil.pendown()
	Pencil.begin_fill()
	Pencil.circle(size)
	Pencil.end_fill()

	
def spiral(longitud,angulo,multiplicador):
	if (longitud==0 or abs(longitud) > 1000):
		return
	
	else:
		color(colorear(),colorear())
		forward (longitud)
		left(angulo)
		spiral(longitud-multiplicador,angulo,multiplicador)
		return

def cono (start):
	speed('fastest')
	if start < 6:
		return
	else:
		
		color(colorear(),colorear())
		#pencolor(colorear())
		width(2)
		begin_fill()
		#fillcolor(colorear())
		circle(start)
		end_fill()
		
		left(90)
		penup()
		forward(6)
		right(90)
		pendown()
		return cono(start - 6)
	bye()
	

			
def main():
	#side = 500
	#myside = side
	#triangulo (myside)
	#side = 0
	#myside = side

	#cuadrado (myside)
	#circulo(turtle,colorear(),50,125,-125)
	
	
	#penup()
	#goto (-200,0)
	#pendown()
	
	
	
	#vowels('ath')
	penup()
	goto (-200,-200)
	pendown()
	spiral(300,60,2)
	
	"""penup()
	goto (-200,0)
	pendown()
	arbol1( 180, 2 )
	"""
main()

