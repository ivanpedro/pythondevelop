
def prefix_average1(S):
	"""Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
	
	n = len(S)
	A = [0] * n #create new list of n zeros
	
	for j in range (n):
		total = 0
	
		for i in range(j + 1):
			# begin computing S[0]+ .... + S[j]
			#1+2+3+... +n
			total +=S[i]
		#record the average
		A[j] = total / (j+1)
	
	return A
	
#Asymptotic Analysis

def prefix_average2(S):
	
	n = len(S)
	A = [0]* n
	
	for j in range(n):
		A[j] = sum (S[0:j+1])/(j+1)
		
	return A
	
#Linear-Time Algorithm	


def  main():
    
    S = [1,2,3,4,5,6,7,8,9]	
    print(prefix_average2(S))


if __name__ == '__main__':

    main()