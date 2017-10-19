#"""
#How the funsion Filter works?

#filter extracts each element in the sequence for which the function returns True.

#"""
#create a list of values for -5 to 5
lista =list(range(-5,5))

#print the list
print('"This is the list to by filtered"')
print(lista)

#make a list from the values filtered with lambda funsion that returns values x <0:
result = list(filter((lambda x : x < 0), lista))
print(' "This is the list filtered with paterns x < 0:"')
print (result)

#other way to achieve the same result

result = []
for x in range(-5,5):
    if x < 0:
         result.append( x)

print (result)
    