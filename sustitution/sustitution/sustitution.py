#sustitution 

def sumProblemString(x, y):
    sum = x + y
    return 'The sum of {} and {} is {}.'.format(x, y, sum)

def cuadrado (value):
    return value**2

def main ():
	a=float (input("Enter value :")) 
	b=float (input("Enter value :"))
	print (sumProblemString (a,b))

	print ("a^2 =",cuadrado(a))
	
main ()

