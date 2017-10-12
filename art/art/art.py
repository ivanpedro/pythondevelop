from turtle import *
from math import *
from random import *
import turtle




def colorear():
	c =  ['green','red','blue','yellow','orange',
	'purple','brown','pink','violet','lightblue',
	'lightpink','lightgreen','lime', '#28e078', '#afc8f9']
	return choice(c)
	
def art (L , N):
	hideturtle()
	speed('fast')
	if N == 0:
		forward(L)
		backward(L)
		return
	
	else:
		color(colorear(),colorear())
		begin_fill()
		forward(L)
		left (60)
		forward(L/2)
		right (180)
		forward(L/2)
		right(3)
		end_fill()
		art (L , N-1)
		#right(6)
		#art (L , N-1)
	return
	
def main():
	
	penup()
	goto (0,0)
	pendown()
	longitud= float(input("Enter longitud :"))
	nivel= float(input("Enter nivel :"))
	art(longitud, nivel)
	
main()
