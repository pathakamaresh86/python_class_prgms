#!/usr/bin/python
import pickle
import os
class Card(object):
	
	def __init__(self):
		self.cardNumber = 1
		self.__cardPin = 1900
		if os.path.exists("card.txt"):
			card_file=open("card.txt",'r')
			card_dict=pickle.load(card_file)
			card_file.close()
			for cardno in card_dict.keys():
				if self.cardNumber < cardno:
					self.cardNumber = cardno
				if self.__cardPin < card_dict[cardno]:
					self.__cardPin = card_dict[cardno]         
			self.cardNumber = self.cardNumber + 1
			self.__cardPin = self.__cardPin + 1
		self.cardType = "Debit"
		
	def getCardPin(self,cardNo):
		return self.__cardPin
		
class BankAccount:

	cards = {}
	def __init__(self,acct_no,name,balance):
		self.name = name
		self.balance = balance
		self.account_no = acct_no
		self.card = Card()
		if os.path.exists("card.txt"):
			card_file=open("card.txt",'r')
			BankAccount.cards=pickle.load(card_file)
			card_file.close()
		BankAccount.cards[self.card.cardNumber]= self.card.getCardPin(self.card.cardNumber)
		card_file=open("card.txt",'w')
		pickle.dump(BankAccount.cards,card_file)
		card_file.close()
		

	def withdraw(self, amount):
		if self.balance < amount:
			return -1
		self.balance = self.balance - amount
		return self.balance
	
	def deposit(self, amount):
		self.balance =self.balance + amount
		return self.balance
		
	def balanceCheck(self):
		return self.balance
		
	def getCardNo(self):
		return self.card.cardNumber
	
	def getCardPin(self,cardNo):
		card_file=open("card.txt",'r')
		BankAccount.cards=pickle.load(card_file)
		card_file.close()
		return self.cards[cardNo]

class Bank:
	bank_id = 1
	accounts = {}
	def __init__(self):
		self.name="ABC"
		
	def authentication(self,cardNo,cardPin):
		acct_file=open("accounts.txt",'r')
		Bank.accounts=pickle.load(acct_file)
		acct_file.close()
		acct=Bank.accounts[cardNo]
		cPin=acct.getCardPin(cardNo)
		if cardPin == cPin:
			return True
		else:
			return False
		
	def createAccount(self,name,balance=0):
		max_acct_no=1
		if os.path.exists("accounts.txt"):
			acct_file=open("accounts.txt",'r')
			Bank.accounts=pickle.load(acct_file)
			acct_file.close()
			for item in Bank.accounts.values():
				if max_acct_no < item.account_no:
					max_acct_no = item.account_no
			max_acct_no = max_acct_no + 1
		print max_acct_no
		acct=BankAccount(max_acct_no,name,balance)
		cardNo=acct.getCardNo()
		Bank.accounts[cardNo] = acct
		acct_file=open("accounts.txt",'w')
		pickle.dump(Bank.accounts,acct_file)
		acct_file.close()
		print Bank.accounts
		
	def deposit(self,cardNo,amount):
		acct=Bank.accounts[cardNo]
		balance=acct.deposit(amount)
		Bank.accounts[cardNo] = acct
		acct_file=open("accounts.txt",'w')
		pickle.dump(Bank.accounts,acct_file)
		acct_file.close()
		print "Your account balance is ", balance
		
	def withdraw(self,cardNo,amount):
		acct=Bank.accounts[cardNo]
		balance=acct.withdraw(amount)
		if balance == -1:
			print "You dont have sufficient balance"
		else:
			Bank.accounts[cardNo] = acct
			acct_file=open("accounts.txt",'w')
			pickle.dump(Bank.accounts,acct_file)
			acct_file.close()
			print "Your account balance is ", balance
		
	def balanceCheck(self,cardNo):
		acct=Bank.accounts[cardNo]
		balance=acct.balanceCheck()
		print "Your account balance is ", balance
		
			
	
class ATM:

	#bank = Bank()
	def __init__(self, bank,cardNo, cardPin):
		self.cardNum = cardNo
		self.cardPinNum = cardPin
		self.bank = bank
		
	def ATMmenu(self):
		ch = -1
		while ch < 1 or ch > 4:
			print("Welcome To ATM Menu !!!")
			print("1.Deposit\n2.Withdraw\n3.Balance Check\n4.Exit")
			ch = input("Enter Choice: ")
		return ch
		
	def showATMOptions(self):
		#bank = Bank()
		isValidCredentials = self.bank.authentication(self.cardNum,self.cardPinNum)
		if isValidCredentials:
			ch = self.ATMmenu()	
			while(ch != 4):
				if ch == 1:
					amount=input("Enter amount to be deposited: ")
					ret=self.bank.deposit(self.cardNum,amount)
				elif ch == 2:
					amount=input("Enter amount to be withdraw: ")
					ret=self.bank.withdraw(self.cardNum,amount)
				elif ch == 3:
					ret=self.bank.balanceCheck(self.cardNum)
				else:
					break
				ch = self.ATMmenu()
		else:
			print "Invalid credentials!!!!"

def menu():
	ch = -1
	while ch < 1 or ch > 3:
		print("Welcome To ABC BANK !!!")
		print("Please select the appropriate Menu: ")
		print("1.Create Account\n2.Show ATM Options\n3.Exit")
		ch = input("Enter Choice: ")
	return ch
	
def main():
	bank=Bank()
	ch = menu()	
	while(ch != 3):
		if ch == 1:
			print "Creating your account!! \nPlease provide your details:"
			AcctName = input("Enter your name: ")
			AcctBalance = input("Enter opening balance: ")
			bank.createAccount(AcctName,AcctBalance)
		elif ch == 2:
			custNo = input("Enter Card Number: ")
			custPin = input("Enter Pin number: ")
			atm = ATM(bank,custNo,custPin)
			#print atm.__dict__
			atm.showATMOptions()
		else:
			break
		ch = menu()
	
if __name__ == "__main__":
	main()

	
