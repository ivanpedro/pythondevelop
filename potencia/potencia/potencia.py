from math import *

#recurcion
#'a =%d y b = %d' % (a,b)

def potencia(b,p):
	"""Calculation of base^power using recurcion"""
	if p == 0:
		return 1
		
	elif p > 0:
		return b* potencia(b,p -1)
	
	else:
		return 1.0/b* potencia(b,p+1)


def main():

	base = float (input ("Enter base:"))
	power = float(input ("Enter power: "))
	print("%d ^ %d = " % (base, power), potencia(base,power))
	
main()

