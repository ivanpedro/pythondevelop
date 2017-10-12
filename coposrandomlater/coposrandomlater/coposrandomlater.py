from turtle import *
from math import *
from random import *
import random, string
import turtle


def colorear():
	c =  ['green','red','blue','yellow','orange',
	'purple','white', 'white','brown','pink','violet','lightblue',
	'lightpink','lightgreen','lime', '#28e078', '#afc8f9']
	return choice(c)
 
fact = (2.0/(3.0*sqrt(3.0)), sqrt(3.0)/2.0, 0.5)

def writers(cx, cy, lengthside, levels):
    
	if levels == 0:
		color(colorear())
		penup()
		goto(cx, cy)
		pendown()
		#forward(lengthside)
		write(random.choice(string.printable))
		return
		
	r = lengthside * fact[0]
	a = r * fact[1]
	b = r * fact[2]
		
	centers = [(cx, cy), (cx, cy+r), (cx, cy-r), (cx+a, cy+b), (cx+a, cy-b), (cx-a, cy+b), (cx-a, cy-b)]
   
	for ux, uy in centers:
		writers(ux, uy, lengthside/3.0, levels-1)

		
if __name__ == "__main__":
    speed(500)
    length = 600.0
    writers(0.0, 0.0, length, 4)
    mainloop()

