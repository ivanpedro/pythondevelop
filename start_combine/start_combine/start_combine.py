from turtle import *
from math import *
from random import *
import turtle


def colorear():
	c =  ['green','red','blue','yellow','orange',
	'purple','brown','pink','violet','lightblue',
	'lightpink','lightgreen','lime', '#28e078', '#afc8f9']
	return choice(c)


def copos(sidelength,levels):
	#L=(sidelength/3)**levels
	if (levels == 0 ):
		for i in range (3*4**levels):
			pencolor(colorear())
			forward(sidelength/3**levels)
			left(120)
		return
                
	#elif (levels == 1):
	else:       
		color(colorear(),colorear())
		begin_fill()
		forward(sidelength/3**levels)
		right(60)
		forward(sidelength/3**levels)
		left(120)
		forward(sidelength/3**levels)
		right(60)
		forward(sidelength/3**levels)
		left(120)
		
		forward(sidelength/3**levels)
		right(60)
		forward(sidelength/3**levels)
		left(120)
		forward(sidelength/3**levels)
		right(60)
		forward(sidelength/3**levels)
		left(120)
		
		forward(sidelength/3**levels)
		right(60)
		forward(sidelength/3**levels)
		left(120)
		forward(sidelength/3**levels)
		right(60)
		forward(sidelength/3**levels)
		left(120)
		end_fill()
		#copos(sidelength,levels-1)
		
	copos(sidelength,levels-1)

	
def main():
	penup()
	goto (-200,0)
	pendown()
	copos(400,7)
	
main()
