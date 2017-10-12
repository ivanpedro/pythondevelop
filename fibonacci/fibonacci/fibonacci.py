#FIBONACCI
import time
from math import *

def fib (n):
	if n <=1:
		return n
	else:
		f= fib(n-1)+fib(n-2)
		return f
		

t0 = time.clock()
n = int (input ("Enter interger value:" ))
result = fib(n)
t1 = time.clock()

print("fib({0}) = {1}, ({2:.2f} secs)".format(n, result, t1-t0))

