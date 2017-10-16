"""
to get reference go to: http://www.bbc.co.uk/bitesize/standard/maths_ii/numbers/compound_interest/revision/1/
P (principal) is the amount borrowed.
R is the rate of interest per year.
T is the time in years.
"""

L = float(input("Enter Loan amout: "))
i = float(input("Enter the interest: "))
Y = float(input("Enter number of payments: "))

def simple_interest(i,L,Y):
    
    if Y == 0:
        return 0
  
    else:     
        return (i/100) * L + simple_interest(i,L,Y-1)

result= simple_interest(i,L,Y)

print("Interest for {} years  : £ {}".format(Y, result))
print("Principal after {} years = £ {}".format(Y, L+result))

def compound_interest(i,L,Y):
   
    if Y == 0:
        return 0
  
    else:     
        return (i/100) * L + compound_interest(i,L+(i/100 *L),Y-1)

result= compound_interest(i,L,Y)

print("The total interest charged under compound interest will be : £ {}".format(result))
print("Principal after {} years = £ {}".format(Y, L+result))
