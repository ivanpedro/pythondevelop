#fatorial

def fac (x):
	if x == 0:
		return 1
	else:
		return x*fac(x-1)
		
		


def main ():
		print ("\"Enter value or E for exit\"")
		c =str ()
		a =int  ()
		
		while c != "E":
				c= input("Enter value: ")
				c = c.upper()
					
				if c != "E":
					a = int(c)
					b = fac (a)
					print (a,"!", "= ", b)

		print("good bye")

	
main()

