from turtle import *
from random import *


def colorear():
    c =  ['green','red','blue','yellow','orange',
	'purple','brown','pink','violet','lightblue',
	'lightpink','lightgreen','lime', '#28e078', '#afc8f9']
    return choice(c)

def pentagonoshapes():
    side = int(input("Enter the amount of sides: "))
    for i in range(side):
        begin_fill()
        forward(200)
        right(360/side)
        for i in range(side):
            color(colorear(),colorear())
            forward(100)
            right(360/side)
            end_fill()

def __main__():
    pentagonoshapes()

__main__()