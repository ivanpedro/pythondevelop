import sys

a = float (input('Enter value to devide:'))
b = float (input('Enter value to devide:'))


try:
	result = a/ b
	print (result)

except ZeroDivisionError:
	print('The answer is infinity')
	
	
"""
#test with this code first to find the name of the error
except:
	error = sys.exc_info()[0]
	print(error)
	
finally :
	print('I will always run')
"""
