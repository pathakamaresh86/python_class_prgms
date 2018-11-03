#!/usr/bin/python

class Human:

	#class attribute
	country = "India"
	#constructor
	def __init__(self,name,address,adhar_no):
		print "self",self
		self.name=name	#object attribute
		self.address=address #object attribute
		self.adhar_no=adhar_no #object attribute
		print("Constructor is invoked for %s" %name)
		
	#destructor
	def __del__(self):
		print("Destructing %s" %self.name)
		
	#Getter
	def getname(self):
		return self.name
		
	#setter
	def setname(self, n):
		self.name=n
	
	def addDOB(self,dob):
		self.dob=dob
	
	def getDOB(self):
		return self.dob
	
def main():
	h1=Human("Amaresh","Pune",123456) #calling constructor
	print h1.getname() #getter
	print h1
	h1.setname("Pranjali") #setter
	print h1.getname()
	print h1
	h1.addDOB("19/11/1986") #Created new dob object variable and pass value to it
	print(h1.getDOB()) #Access dob value
	print h1.__dict__ #Object is dict so Print dict 
	print Human.country #Class variable
if __name__=="__main__":
	main()

'''
D:\F DATA\python_class>python oop_concepts.py
self <__main__.Human instance at 0x0000000003263548>
Constructor is invoked for Amaresh
Amaresh
<__main__.Human instance at 0x0000000003263548>
Pranjali
<__main__.Human instance at 0x0000000003263548>
19/11/1986
{'dob': '19/11/1986', 'name': 'Pranjali', 'adhar_no': 123456, 'address': 'Pune'}
India
Destructing Pranjali
'''