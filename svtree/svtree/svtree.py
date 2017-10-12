from turtle import *
from math import *
from random import *
import turtle
import random, string


def colorear():
	c =  ['green','red','blue','yellow','orange',
	'purple','brown','pink','violet','lightblue',
	'lightpink','lightgreen','lime', '#28e078', '#afc8f9']
	return choice(c)

def svtree( trunklength, levels ):
	""" our chai function! """
	if (trunklength  <9 ):
		return
		
	else:
		color(colorear(),colorear())
		forward(trunklength)
		write(choice(string.printable))
		left(45)
		forward(trunklength/2.0)
		right(45)
		svtree( trunklength/2.0, levels )
		right(45)
		right(90)
		forward(trunklength/2.0)
		left(90)
		forward(trunklength/2)
		left(45)
		svtree( trunklength/2, levels )
		left (45)
		left(90)
		forward(trunklength/2)
		left(45)
		left (180)
		backward(trunklength)
		return 
		
def main():
	
	penup()
	goto (-200,100)
	pendown()
	longitud = float (input ("Enter longitud:"))
	nivel = float(input ("Enter nivel: "))
	
	svtree(longitud,nivel)
	
	
main()

