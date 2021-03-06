from turtle import *
from math import *
from random import *
import turtle

import random, string

def colorear():
	c =  ['green','red','blue','yellow','orange',
	'purple','white','brown','pink','violet','lightblue',
	'lightpink','lightgreen','lime', '#28e078', '#afc8f9']
	return choice(c)
	
def snowflake(sidelength, levels):
    
	#color(colorear(),colorear())
	def flakeside(sidelength, levels):	
		if levels == 0:
			color(colorear(),colorear())
			forward(sidelength)
			write(choice(string.printable))
			
		else:
			
			for angle in [60,-120,60,0]:
				flakeside(sidelength/3, levels-1)	
				right(angle)
	
	for i in range (3):
		flakeside(sidelength, levels)
		left(120)	
	
def main():
	
	
	
	speed(500)
	penup()
	goto (-200,-150)
	pendown()
	begin_fill()
	snowflake(500, 5)
	end_fill()
	

	exitonclick()
	
main()

