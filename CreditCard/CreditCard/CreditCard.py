
#class creadit card
#CamelCase convention for classess

class CreditCard:
	""" A consumer credit card"""
	# class contructor
	def __init__(self, customer, bank, acnt, limit):
		""" Create a new credit card instance.
		customer the name of the customer (e.g., John Bowman )
		bank the name of the bank (e.g., California Savings )
		acnt the acount identifier (e.g., 5391 0375 9387 5309 )
		limit credit limit (measured in dollars)
	
		"""
		#instances variables
		#_customer mean that it is an internal
		self._customer = customer
		self._bank = bank
		self._account = acnt
		self._limit = limit
		self._balance = 0
		
	#instance method
	#method or funtion should be a verb that discribe its effect. 
	def get_customer(self):
		""" returns the name of the customer"""
		return self._customer
		
	def get_bank(self):
		""" returns the name of the bank"""
		return self._bank
		
	def get_account(self):
		""" returns the account number """
		return self._account
		
	def get_limit(self):
		"""returns the current credit limit's account."""
		return self._limit
		
	def get_balance(self):
		"""returns the current balance of the account."""
		return self._balance
		
	def charge(self, price):
		"""Charge given price to the card, assuming sufficient credit limit.
		
		Returns True if charg was processed; False if charge was denied.
		"""
		
		if price + self._balance > self._limit : #if charge would excedd limit
			return False                         # cannot accept charge
			
		else:	
			self._balance += price
			return True
		
	def make_payment(self, amount):
		"""Process customer payment that reduces balance."""
		self._balance -= amount
		
		
#The constructor

#cc = CreditCard('Ivan Pedro', 'Bank Metropolitano',
# "5555 6666 4444 2020", 1000 )

#print(cc._account)


if __name__ == '__main__':

	wallet = []

	wallet.append(CreditCard('Ivan Pedro', 'Bank Metropolitano',
                         "5555 6666 4444 2020", 9000))

	wallet.append(CreditCard('Jose Ramon', 'Bank Spanin',
                         "9999 6666 4444 2020", 3000))
						 
	wallet.append(CreditCard('Natividad Cuervo', 'Bank Cuba',
                         "1010 6666 4444 2020", 5000))
						 
	for val in range(1, 17):
		wallet[0].charge(val)
		wallet[1].charge(2*val)
		wallet[2].charge(3*val)
						 
	for c in range(3):
		print('Customer =', wallet[c].get_customer())
		print('Bank =', wallet[c].get_bank())
		print('Account =', wallet[c].get_account())
		print('Limit =', wallet[c].get_limit())
		print('Balance =', wallet[c].get_balance())
		while wallet[c].get_balance() > 100:
			wallet[c].make_payment(100)
			print('New balance =', wallet[c].get_balance())
		print(wallet[0])
