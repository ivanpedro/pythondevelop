
from turtle import *
from math import *
from random import *
import turtle


def colorear():
	c =  ['green','red','blue','yellow','orange',
	'purple','white', 'white','brown','pink','violet','lightblue',
	'lightpink','lightgreen','lime', '#28e078', '#afc8f9']
	return choice(c)

def flakeside(sidelength,levels):
	speed('fastest')
	if (levels == 0 ):
		for i in range (3*4**levels):
			pencolor(colorear())
			forward(((sidelength/3)))
			left(120)
		return

	elif (levels == 1):
			
			for i in range (3*4**levels):
				color(colorear(),colorear())
				begin_fill()
				forward(sidelength/3**levels)
				right(60)
				forward(sidelength/3**levels)
				left(120)
				forward(sidelength/3**levels)
				right(60)
				forward(sidelength/3**levels)
				right(60)
				end_fill()
			
	else :
		right(60)
		flakeside(sidelength,levels -1)
	
	
	
	
def main():
	
	penup()
	goto (0,0)
	pendown()
	flakeside(100,10)
	
main()
