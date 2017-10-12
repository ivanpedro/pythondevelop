# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 16:22:46 2017

@author: Ivan
"""

class Parent():
    """This class provide guidances examples for inheritance in Python"""
    # class contructor
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        #instance Variable
        self.last_name = last_name
        self.eyes_color = eye_color
        
    #instance method
    def show_info(self):
        print("Last Name: " +  self.last_name)
        print("Eyes Color: " + self.eyes_color)
            
#parent means that Child inherits from Parent        
class Child(Parent):
    #Constructor of Child Class
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor Called")
        Parent.__init__(self,last_name, eye_color)
        self.number_of_toys = number_of_toys
        
    #Method Override
    def show_info(self):
         print("Last Name: " + self.last_name)
         print("Eyes Color: " + self.eyes_color)
         print("Number of Toys: " + str( self.number_of_toys))

#test the Parent class        
billy_cyrus = Parent("Cyrus", "Blue")
#print(billy_cyrus.last_name)
#billy_cyrus.show_info()


#test of Child class

miley_cyrus = Child("Cyrus", "Blue", 5)
#print(miley_cyrus.last_name)
#print(miley_cyrus.number_of_toys)
miley_cyrus.show_info()

