from turtle import *
from math import *
from random import *
import turtle


def colorear():
	c =  ['green','red','blue','yellow','orange',
	'purple','white','brown','pink','violet','lightblue',
	'lightpink','lightgreen','lime', '#28e078', '#afc8f9']
	return choice(c)
	
def misubishi(sidelength,levels):
	speed('fastest')
	if (levels == 0 ):
		for i in range (3*4**levels):
			pencolor('green')
			forward(((sidelength/3)))
			left(120)
		return
		
	elif (levels >= 1):
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
			right(120)
			end_fill()
	right(30)		
	misubishi(sidelength,levels)		
			
			
def main():
	
	penup()
	goto (0,0)
	pendown()
	misubishi (200,1)
	
main()

