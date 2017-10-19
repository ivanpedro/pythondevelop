"""map, filter, and reduce
Using map, filter, reduce, write a code that create a list of 
(n)**2 for range(10) for even integers:

"""

from functools import reduce

#l = [x for x in range(10) if x % 2 == 0]
#print (l)

#m = filter(lambda x:x % 2 == 0, [x for x in range(10)] )
#print (m)

#o = map(lambda x: x**2, m)
#print (o)

#p = reduce(lambda x,y:x+y, o)
#print (p)

#comprehension: finding intersection of two lists:

a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]

print ([x for x in a if x in b]) # prints out [2, 3, 5, 7]

#filter(): finding intersection of two lists:

print (filter(lambda x: x in a, b))  # prints out [2, 3, 5, 7]