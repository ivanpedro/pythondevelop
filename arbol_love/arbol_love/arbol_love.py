from turtle import *
from math import *
from random import *
import turtle



def colorear():
	c =  ['green','red','blue','yellow','orange',
	'purple','brown','pink','violet','lightblue',
	'lightpink','lightgreen','lime', '#28e078', '#afc8f9']
	return choice(c)

def arbol_love(L , N):
	speed('fastest')
	width (2)
	#speed (choice(['slow','fast','fastest','slowest']))
	if N == 0:
		forward(L/2)
		backward(L/2)
		return
	else:
		color(colorear(),colorear())
		
		forward(L/2)
		left (60)
		forward(L/2)
		right(30)
		arbol_love (L/2, N-1)
		right(150)
		forward(L/2)
		
		#secund part
		left(60)
		forward(L/2)
		
		left(30)
		arbol_love (L/2, N-1)
		left (150)
		forward(L/2)
		right (120)
		backward(L/2)
			
		
def main():
	
	penup()
	goto (-200,100)
	pendown()
	longitud = float (input ("Enter longitud:"))
	nivel = float(input ("Enter nivel: "))
	
	arbol_love(longitud,nivel)
	
	
main()

