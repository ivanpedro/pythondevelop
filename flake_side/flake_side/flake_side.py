from turtle import *
from math import *
from random import *
import turtle


def colorear():
	c =  ['green','red','blue','yellow','orange',
	'purple','white', 'white','brown','pink','violet','lightblue',
	'lightpink','lightgreen','lime', '#28e078', '#afc8f9']
	return choice(c)


def copos(sidelength,levels):
	if levels== 0:
		color(colorear())
		forward (sidelength)
		
	else:
		for angle in [60,-120,60,0]:
			copos(sidelength/3, levels -1)
			right(angle)


			
def main():
	penup()
	goto (-200,0)
	pendown()
	largo = float(input("Enter largo: "))
	nivel = float(input("Enter nivel: "))

	copos(largo , nivel )
	
main()

