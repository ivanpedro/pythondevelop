
from math import *

""" volumen of the cono """

def volumen_cono(rb,h,R):
	v = 1/3* pi* h * (R**2 + rb**2 + R*rb)
	return v

	
def main():
    
	rb= float(input("\"Enter radio of base:\":"))
	h= float(input("\"Enter height\":"))
	R= float(input("\"Enter radio of superior\":"))
	print("The volumen of the Cono is: " , volumen_cono(rb , h , R ), "m3")
	
main ()
