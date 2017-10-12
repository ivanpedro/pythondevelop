
#cesaro
from turtle import *
from math import *
from random import *
import random, string


#write(choice(string.printable))	

def colorear():
	c =  ['green','red','blue','yellow','orange',
	'purple','white', 'white','brown','pink','violet','lightblue',
	'lightpink','lightgreen','lime', '#28e078', '#afc8f9']
	return choice(c)
	
def cesaro (size,level):
	if level ==0:
		color(colorear())
		forward(size)
	else:	
		for angle in [85,-170,85 ,0]:
			cesaro (size/3,level-1)
			right(angle)


                        
def cesaro_cuadrado(size,level):
    for i in range (4):
        cesaro(size,level)
        left(90)



			
		
def main ():
	speed(500)
	
	cesaro_cuadrado (600,4)

	
main ()