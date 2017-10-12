
from turtle import *
from math import *
from random import *
import turtle

# 'a =%d y b = %d' % (a,b) sustitucion en cadena

#Start Spiral
def colorear():
	c =  ['green','red','blue','yellow','orange',
	'purple','brown','pink','violet','lightblue',
	'lightpink','lightgreen','lime', '#28e078', '#afc8f9']
	return choice(c)

def arbol1 (L , N):
	#speed (choice(['slow','fast','fastest','slowest']))
	if N == 0:
		forward(L)
		backward(L)
		return
	else:
		color(colorear(),colorear())
		
		forward(L)
		left (60)
		forward(L/2)
		right(30)
		arbol1 (L/2 , N-1)
	
		right(150)
		forward(L/2)
		
		#secund part
		left(60)
		forward(L/2)
		
		right (30)
		arbol1 (L/2 , N-1)
		right (150)
		forward(L/2)
		right (120)
		backward(L)

def main():
	
	penup()
	goto (-200,0)
	pendown()
	longitud = float (input ("Enter longitud:"))
	nivel = float(input ("Enter nivel: "))
	arbol1 (longitud ,nivel)
	
	
main()


