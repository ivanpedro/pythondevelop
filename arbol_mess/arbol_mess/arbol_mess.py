
from turtle import *
from math import *
from random import *
import turtle



def colorear():
	c =  ['green','red','blue','yellow','orange',
	'purple','brown','pink','violet','lightblue',
	'lightpink','lightgreen','lime', '#24e074', '#afc4f9']
	return choice(c)

def arbol (L , N):
	speed('fastest')
	width (2)
	#speed (choice(['slow','fast','fastest','slowest']))
	if N == 0:
		forward(L*3/4)
		backward(L*3/4)
		return
	else:
		color(colorear(),colorear())
		
		forward(L*3/4)
		left (60)
		forward(L*3/4)
		right(30)
		arbol (L*3/4, N-1)
		right(150)
		forward(L*3/4)
		
		#secund part
		left(60)
		forward(L*3/4)
		left(30)
		arbol (L*3/4, N-1)
		left (150)
		forward(L*3/4)
		right (120)
		backward(L*3/4)
			
		
def main():
	
	penup()
	goto (-200,100)
	pendown()
	longitud = float (input ("Enter longitud:"))
	nivel = float(input ("Enter nivel: "))
	
	arbol(longitud,nivel)
	
	
main()
