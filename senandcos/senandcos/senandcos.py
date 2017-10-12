from turtle import *
from math import *
from random import *
import turtle

c = ['green','red','blue','yellow','orange','lightblue','brown'
,'purple','black','pink','magenta']

def circulo (x,y,w,c,radio):
	
	penup()
	goto(x,y)
	width (w)
	pendown()
	color(choice(c),choice(c))
	begin_fill()
	circle(radio)
	end_fill()

def coseno(angle):
	for y in range (angle):
		x=cos(randians( y))
		goto(x,y)
		
def seno (angle):
	for x in range (angle):
		y=sin(radians(x))
		goto(x,y)

def main():
	wn = turtle.Screen()
	#wn.setworldcoordinates(-500,-1,1000,1)
	wn.setworldcoordinates(-500,-500,1000,1000)
	wn.bgcolor(choice(c))

	fred = turtle.Turtle()
	
	for x in range (2*360):
		y=sin(radians(x))
		fred.goto(x,y)

	
	circulo(0,0,2,c,200)
	
	
	wn.exitonclick()
	
	
main ()

