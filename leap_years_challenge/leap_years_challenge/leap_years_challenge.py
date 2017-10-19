"""
In the Gregorian calendar three criteria must be taken into account to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
    The year can be evenly divided by 100, it is NOT a leap year, unless:
        The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years,
while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years
The year is a leap year (it has 366 days).
The year is not a leap year (it has 365 days).
"""

#import sys

#year = float (input('Enter year: '))

#try:
#    def leap_year(year):
#    #The year can be evenly divided by 4 with no remainder,it  is a leap year unless:
#        if year % 4 == 0:
#            #The year can be evenly divided by 100, it is NOT a leap year, unless
#            if year % 100 == 0:
#                #The year is also evenly divisible by 400. Then it is a leap year.
#                if year % 400 == 0:
#                    return True
                    
#        return False

#    leap_year(year)      

##test with this code first to find the name of the error
#except :
#	error = sys.exc_info()[0]
#	print(error)
	
#finally :
#	print('I will always run')



year = float (input('Enter year: '))

def leap_year(year):
    #The year can be evenly divided by 4 with no remainder,it  is a leap year unless:
    if year % 4 == 0:
    #The year can be evenly divided by 100, it is NOT a leap year, unless
        if year % 100 == 0:
            #The year is also evenly divisible by 400. Then it is a leap year.
            if year % 400 == 0:
                print('Leap year')
                return True
    print('No Leap year')            
    return False 
     
#test with this code first to find the name of the error

leap_year(year)

