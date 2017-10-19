"""
Read an integer N.

Without using any string methods, try to print the following:
input = 3
output =123


"""

#n=int(input("enter n value:"))
#r =str (x for x in range(n))
#print(r)

if __name__ == '__main__':
    n=int(input("enter n value:"))
    
    result = ''
    for i in range(n):
        result = result + str(i +1)

    print(result)
       
