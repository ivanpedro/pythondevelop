def vowels(s):
	"""Calculate the number of vowels in the string"""
	vowel= ['a', 'e', 'i', 'o','u']
	if s == '':
		return 0
	elif s[0] in vowel:
		return 1+ vowels(s[1:])
	else:
		return vowels(s[1:])
		
def main():

	string= str (input("Enter string:"))
	print(' amount of vowels: %d ' % (vowels(string)))
	
main()

