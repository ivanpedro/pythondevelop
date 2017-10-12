from turtle import *
from math import *
from random import *
import turtle

def colorear():
	c =  ['green','red','blue','yellow','orange',
	'purple','brown','pink','violet','lightgreen','lime','lightpink',
    'lightblue','lightred','#28e078','#afc8f9', '#28f250','#98f250']
	return choice(c)
	
	
def snowflake(sidelength, levels):

	def flakeside(sidelength, levels):	
		if levels == 0:
			color(colorear(),colorear())
			begin_fill()
			forward(sidelength/3**levels)
			left(120)
			forward(sidelength/3**levels)
			left(120)
			forward(sidelength/3**levels)
			left(120)
			end_fill()
			return
			
		elif levels == 1:
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
			return
			
	flakeside( sidelength, levels )
	left(120)
	flakeside( sidelength, levels )
	left(120)
	flakeside( sidelength, levels )
	left(120)
	flakeside( sidelength, levels )
	left(120)
	snowflake(sidelength, levels-1)
	return
	
	bye()
	
			
	
	
def main():
	
	penup()
	goto (0,0)
	pendown()
	snowflake(100, 1)
	
	
main()
