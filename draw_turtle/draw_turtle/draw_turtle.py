
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 23:42:27 2017

@author: Ivan
"""
from random import *
import turtle

def colorear():
	c =  ['green','red','blue','yellow','orange',
	'purple','brown','pink','violet','lightblue',
	'lightpink','lightgreen','lime', '#28e078', '#afc8f9']
	return choice(c)

def draw_art():
    
    window =  turtle.Screen()
    window.bgcolor("pink")
    
    brad = turtle.Turtle()
    brad.color(colorear())
    brad.speed(10)
    brad.shape("turtle")
    brad.goto(-100,-100)
    
    for i in range(36):
        brad.color(colorear())
        draw_pentagono(brad)
        brad.right(10)
        
    brad.penup()
    brad.goto(100,100)
    brad.pendown()
    
    for i in range(36):
        brad.color(colorear())
        draw_circle(brad)
        brad.right(10)
        
    window.exitonclick()
    
   
def draw_square(name):
   
    for i in range(4):
        name.forward(100)
        name.right(90)

        
def draw_pentagono(p):
    for i in range(5):
        p.forward(100)
        p.left(360/5)

def draw_trian(t):
    for i in range(3):
        t.forward(100)
        t.left(120)
        
  

def draw_circle(c):
    
    c.circle(100)
    
    

def __main__():
    ivan = draw_art()
    print(ivan)

__main__()