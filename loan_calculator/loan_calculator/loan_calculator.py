#import datetime

#currentDate= datetime.date.today()
#print (currentDate)
#print(currentDate.month)
#print(currentDate.day)
#print(currentDate.year)

#print(currentDate.strftime('%d %b, %Y'))
#print(currentDate.strftime("%d /%B / %Y"))


#userInput = input('Please enter your birthday (mm/dd/yyyy)')
#birthday = datetime.datetime.strptime(userInput, '%m/%d/%Y').date()
#print(birthday)
#days = birthday - currentDate
#print(days.days)

"""
have the user enter the cost of the loan, the interest rate, an the number of years for the loan
calculate mothly payment eiht the following formula

M = monthly payment
L = Loan amout
i = interest rate (for an interest rate of 5%, i = 0.005)
n = number of payments


"""

L = float(input("Enter Loan amout: "))
i = float(input("Enter the interest: "))
n = float(input("Enter number of payments: "))


#M = L*[i*(1+i)*n]/[(1+i)*n - 1] 

#print ("Enter your monthly payment: £ %f" % (M))
#print(M*36)
#print ("Your monthly payment: £ {}".format(M))

