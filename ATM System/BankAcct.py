#!/usr/bin/python
from card import Card
import pickle
class BankAccount:

	acct_no = 1# class attribute
	def __init__(self, name, balance = 0):
		self.name = name
		self.balance = balance
		self.acct_no = BankAccount.acct_no
		BankAccount.acct_no = BankAccount.acct_no + 1

	def withdraw(self, amount):
		if self.balance < amount:
			return -1
		self.balance = self.balance - amount
		return self.balance

	def deposit(self, amount):
		self.balance =self.balance + amount

def main():
	EmployeeList=[]
	InactiveEmpList=[]
	pickle_inp=input("Do you want to load the persisted employee records (y/n): ")
	if pickle_inp == 'y':
		emp_file=open("emp_rec.txt",'r')
		resigned_emp_file=open("resign_emp_rec.txt",'r')
		EmployeeList=pickle.load(emp_file)
		InactiveEmpList=pickle.load(resigned_emp_file)
		emp_file.close()
		resigned_emp_file.close()
	emp1=Employee("Amaresh","Pune",9850728760,12345,"Male",10000,"Team Lead","Pune","Development","BRM")
	print emp1.__dict__
	print
	emp2=Employee("abc","mumba",3456,8907,"Male",20000,"SE","Pune","Testing","PQR")
	emp3=Employee("ram","nagpur",34256,890745,"Male",30000,"SSE","Mumbai","PE","SQA")
	EmployeeList.append(emp1)
	EmployeeList.append(emp2)
	EmployeeList.append(emp3)
	print EmployeeList
	rem_emp=input("Enter empid to be removed")
	for emp in EmployeeList:
		if emp.empid == rem_emp:
			InactiveEmpList.append(emp)
			EmployeeList.remove(emp)
	print EmployeeList
	print InactiveEmpList
	empid=input("Enter empid to be updated")
	updated_addr=input("Enter updated address")
	
	for emp in EmployeeList:
		if emp.empid == empid:
			emp.UpdateAddr(updated_addr)
			print emp
	print EmployeeList
	emp_file=open("emp_rec.txt",'a')
	resigned_emp_file=open("resign_emp_rec.txt",'a')
	pickle.dump(EmployeeList,emp_file)
	pickle.dump(InactiveEmpList,resigned_emp_file)
	emp_file.close()
	resigned_emp_file.close()
	
	
if __name__=="__main__":
	main()
	
'''
[Employee number 1--->Amaresh--=>Pune, Employee number 2--->abc--=>mumba, Employee number 3--->ram--=>nagpur]
Enter empid to be removed2
[Employee number 1--->Amaresh--=>Pune, Employee number 3--->ram--=>nagpur]
[Employee number 2--->abc--=>mumba]
Enter empid to be updated3
Enter updated address"Goa"
Employee number 3--->ram--=>Goa
[Employee number 1--->Amaresh--=>Pune, Employee number 3--->ram--=>Goa]
sanketoswal123@gmail.com
'''
