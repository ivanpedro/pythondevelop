#cesaro
from turtle import *
from math import *
from random import *
import random, string


def piramide (size, level):
	if level == 0:
		for i in range (3):
			forward(size)
			left (120)
	else:
		coord =[(0,0),(size/2,0),(size/4,(size/2) + sin(60))]
		
		for x,y in coord:
			penup()
			goto(x,y)
			pendown()
			piramide (size, level-1)
			
		
def main ():
    speed(500)
   
    piramide(300,1)
	
main ()

