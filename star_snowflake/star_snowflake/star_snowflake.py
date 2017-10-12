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
		snowflake(120,5)
		left(170)
		if abs(pos()) < 1:
			break
	end_fill()
	done()

def snowflake(sidelength, levels):
    
	#color(colorear(),colorear())
	def flakeside(sidelength, levels):	
		if levels == 0:
			color(colorear(),colorear())
			forward(sidelength)
				
		else:
			
			for angle in [60,-120,60,0]:
				flakeside(sidelength/3, levels-1)	
				right(angle)
	
	for i in range (3):
		flakeside(sidelength, levels)
		left(120)
		
def main ():
	speed(500)
	star()
	
main ()
