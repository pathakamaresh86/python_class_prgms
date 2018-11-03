#!/usr/bin/python

class Account:

	account_no=12345
	
	#constructor
	'''
	class Account:
		#constructor
	'''
	
	def __init__(self,acct_name,acct_mobile_no,acct_adhar_no,acct_balance=0):
		self.acct_name=acct_name
		self.acct_mobile_no=acct_mobile_no
		self.acct_adhar_no=acct_adhar_no
		self.acct_balance=acct_balance
		self.account_no=Account.account_no
		Account.account_no = Account.account_no + 1
	
	def deposit(self,amount):
		self.acct_balance+=amount
		return self.acct_balance
		
	def widraw(self,amount):
		if self.acct_balance < amount:
			print "Account number ",str(self.account_no)," has insufficient balance ",self.acct_balance, " to withdaw ", amount 
			return self.acct_balance
		self.acct_balance-=amount
		return self.acct_balance
	
	def __repr__(self):
		return "Account number " + str(self.account_no) + " balance is " + str(self.acct_balance)
	
def main():
	acc1=Account("Amaresh Pathak",9850728760,12345,10000)
	acc1.deposit(5000)
	print acc1
	
	acc2=Account("Pranjali Pathak",9850728760,12345)
	acc2.deposit(5000)
	acc2.widraw(4000)
	print acc2
	
	acc3=Account("Mayura Pathak",9850728760,12345,5000)
	acc3.deposit(1000)
	acc3.widraw(7000)
	print acc3
	
if __name__=="__main__":
	main()

'''
D:\F DATA\python_class>python oop_accountOpr.py
Account number 12345 balance is 15000
Account number 12346 balance is 1000
Account number  12347  has insufficient balance  6000  to withdaw  7000
Account number 12347 balance is 6000
'''
