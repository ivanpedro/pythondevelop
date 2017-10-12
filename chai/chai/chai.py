from turtle import *
from math import *
from random import *
import turtle


def colorear():
	c =  ['green','red','blue','yellow','orange',
	'purple','brown','pink','violet','lightblue',
	'lightpink','lightgreen','lime', '#28e078', '#afc8f9']
	return choice(c)
	
def chai(size):
	""" our chai function! """
	if (size<3):
		return
		
	else:
		color(colorear(),colorear())
		forward(size)
		left(90)
		forward(size/2.0)
		right(90)
		chai(size/2)
		right(90)
		forward(size)
		left(90)
		chai(size/2)
		left(90)
		forward(size/2)
		right(90)
		backward(size)
		return
	
def main():
	
	penup()
	goto (-200,0)
	pendown()
	longitud = float(input("Enter longitud :"))
	chai(longitud)
	
main()

