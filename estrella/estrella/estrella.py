from turtle import *
from math import *
from random import *
import turtle



def colorear():
	c =  ['green','red','blue','yellow','orange',
	'purple','brown','pink','violet','lightblue',
	'lightpink','lightgreen','lime', '#28e078', '#afc8f9']
	return choice(c)

def estrella(value):
    Pencil = turtle.Turtle ()
    Pencil.speed (0)
    Pencil.hideturtle()
    Pencil.color (colorear())
    Pencil.penup()
	# position of the cursor at the bottom right 
    Pencil.goto(0,0) 
    Pencil.pendown()
    for i in range (1,250):
        value = value + 2 
        Pencil.forward(value)
        Pencil.right(152)
			
		
def main():
	
	penup()
	goto (-200,100)
	pendown()
	longitud = float (input ("Enter longitud:"))
	
	
	estrella(longitud)
hideturtle()	
	
main()

