from turtle import *
from math import *
from random import *
import turtle



def colorear():
	c =  ['green','red','blue','yellow','orange',
	'purple','brown','pink','violet','lightblue',
	'lightpink','lightgreen','lime', '#28e078', '#afc8f9']
	return choice(c)
	
def poly (n,N):
	
	
	if n == 0:
		return
	else:
		
		color(colorear(),colorear())
		begin_fill()
		forward (50)
		left(360/N)
		poly (n-1,N)
		end_fill()
		return
		
def main():
	
  
	penup()
	goto (0,0)
	pendown()
	base = float (input ("Enter base:"))
	power = float(input ("Enter power: "))
	poly(base,power)
	
	
main()

