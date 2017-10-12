from turtle import *
from math import *
from random import *
import turtle



def colorear():
	c =  ['green','red','blue','yellow','orange',
	'purple','brown','pink','violet','lightblue',
	'lightpink','lightgreen','lime', '#28e078', '#afc8f9']
	return choice(c)

def arbol (L , N):
	speed('fastest')
	width (2)
	#speed (choice(['slow','fast','fastest','slowest']))
	if N == 0:
		forward(L*3/8)
		backward(L*3/8)
		return
		
	else:
		color(colorear(),colorear())
		
		forward(L*3/8)
		left (60)
		forward(L*3/8)
		right(30)
		arbol (L*3/8, N-1)
		right(150)
		forward(L*3/8)
		
		#secund part
		left(60)
		forward(L*3/8)
		left(30)
		arbol (L*3/8, N-1)
		left (150)
		forward(L*3/8)
		right (120)
		backward(L*3/8)
			
		
def main():
	
	penup()
	goto (-200,100)
	pendown()
	longitud = float (input ("Enter longitud:"))
	nivel = float(input ("Enter nivel: "))
	
	arbol(longitud,nivel)
	
	
main()

