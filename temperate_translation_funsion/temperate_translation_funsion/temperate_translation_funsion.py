"""
Celsius = [39.2, 36.5, 37.3, 37.8]

Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsiusprint Fahrenheit
[102.56, 97.700000000000003, 99.140000000000001, 100.03999999999999]

C = map(lambda x: (float(5)/9)*(x-32), Fahrenheit)
print C
[39.200000000000003, 36.5, 37.300000000000004, 37.799999999999997]

"""
import sys

def fahrenheit(T):
    return ((float(9)/5)*T + 32)

def celsius(T):
    return (float(5)/9)*(T-32)

def tempeture ():
   
  while True:
       
        i = input("Enter F to calculate temperature in Fahrenheit | C to calculate temperature in Celsius | Q to exit: ")

        if i.upper() == 'F':
            temp = float(input('Enter temperature value in Celsius: '))
            print ('Temperature in fahrenheit: {} F'.format(fahrenheit(temp)))
            
        elif i.upper() == 'C':
            temp = float(input('Enter temperature value in Fahrenheit: '))
            print ('Temperature in celsius: {} C'.format(celsius(temp)))

        elif  i.upper() == 'Q':
            break 

        else:
            i = input("Enter F to calculate temperature in Fahrenheit | C to calculate temperature in Celsius | Q to exit: ")

def main():
    try:
        tempeture()
        return 0
    except:
        return 1
 
if __name__ == "__main__":
    sys.exit(main())


    
   

