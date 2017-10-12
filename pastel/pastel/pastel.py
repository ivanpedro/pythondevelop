from  turtle import *
from math import *
from random import *

c = ['green','red','blue','yellow','orange',
'purple','black','brown','pink','violet']

def draw_circle(x, y,w,c,radio,angle):
	penup()
	goto(x,y)
	width(w)
	pendown()
	color(choice(c),choice(c))
	begin_fill()
	circle(radio,angle)
	end_fill()
	
def draw_line (x,y,angle,distance):
	penup()
	goto(x,y)
	pendown()
	setheading(angle)
	forward(distance)
	
	
def line_coordinates(x,y,x1,y1):
	penup()
	goto(x,y)
	pendown()
	goto(x1,y1)
	
def part(fraccion):
	#fraccion is porcentage value
	angulo= 2 *pi* fraccion/100
	return angulo
	


def seno (angle):
	for x in range (angle):
		y=sin(radians(x))
		goto(x,y)
	
def main ():
	
	x = 0
	y = 100
	radio = 100
	suspensos = 10
	aprobados = 60
	super = 40
	
	x1=x+radio*cos(part((suspensos)))
	y1=y+radio*sin(part((suspensos)))
	line_coordinates(x,y,x1,y1)
	
	
	draw_circle(0,0,2,c,100,360)
	draw_line(0,100,0,100)
	
	
	x1=x+radio*cos(part(aprobados+suspensos))
	y1=y+radio*sin(part(aprobados+suspensos))
	line_coordinates(x,y,x1,y1)
	
	x1=x+radio*cos(part(aprobados+suspensos+super))
	y1=y+radio*sin(part(aprobados+suspensos+super))
	line_coordinates(x,y,x1,y1)
	
	
	
main ()

