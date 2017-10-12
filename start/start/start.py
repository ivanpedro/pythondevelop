from  turtle import *
from math import *
from random import *



def colorear():
	c =  ['green','red','blue','yellow','orange',
	'purple','white', 'white','brown','pink','violet','lightblue',
	'lightpink','lightgreen','lime', '#28e078', '#afc8f9']
	return choice(c)

def star ():
	color(colorear(),colorear())
	begin_fill()
	while True:
		forward(200)
		left(170)
		if abs(pos()) < 1:
			break
	end_fill()
	done()

def main ():
	
	star()
	
main ()

