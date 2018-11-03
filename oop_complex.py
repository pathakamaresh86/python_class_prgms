#!/usr/bin/python

class complex:

	#constructor
	def __init__(self,real=0,img=0):
		self.real=real	#object attribute
		self.img=img #object attribute
		
	#destructor
	def __del__(self):
		#print "Destructing self", self
		print
	
	def add2ComplexNo(self,c1):
		c3=complex()
		if type(c1)==int:#if isinstance(c1,int):
			c3.real=self.real + c1
			c3.img=self.img
		else:
			c3.real=self.real + c1.real
			c3.img=self.img + c1.img
		return c3
		
	def sub2ComplexNo(self,c1):
		c3=complex()
		c3.real=self.real - c1.real
		c3.img=self.img - c1.img
		return c3

	#Operator opverloading
	def __add__(self,c1):
		c3=complex()
		if isinstance(c1,int):
			c3.real=self.real + c1
			c3.img = self.img
		else:
			c3.real=self.real + c1.real
			c3.img=self.img + c1.img
		return c3
			
	def __sub__(self,c1):
		c3=complex()
		if isinstance(c1,int):
			c3.real=self.real - c1
			c3.img = self.img
		else:
			c3.real=self.real - c1.real
			c3.img=self.img - c1.img
		return c3
		
	def __mul__(self,c1):
		c3=complex()
		c3.real=self.real * c1.real
		c3.img=self.img * c1.img
		return c3
		
	def __eq__(self,c1):
		if self.real == c1.real and self.img == c1.img:
			return True
		return False
		
	def __gt__(self,c1):
		if self.real > c1.real and self.img > c1.img:
			return True
		return False
	
	def __lt__(self,c1):
		if self.real < c1.real and self.img < c1.img:
			return True
		return False
		
	def __ge__(self,c1):
		if self.real >= c1.real and self.img >= c1.img:
			return True
		return False
	
	def __le__(self,c1):
		if self.real <= c1.real and self.img <= c1.img:
			return True
		return False
	
	def __repr__(self):
		return str(self.real) + " + "+ str(self.img) + "i"
	
def main():
	c1=complex(10,8)
	c2=complex(3,2)
	print c1 + c2
	print c1 + 4
	print c1 - c2
	print c1 - 4
	print c1 * c2
	
	print c1 > c2
	print c1 < c2
	print c1 >= c2
	print c1 <= c2
	
	c1=complex(10,8)
	c2=complex(10,8)
	print c1 == c2
	
	'''
	c3 = c1.add2ComplexNo(c2)
	print(c3)
	c3 = c1.add2ComplexNo(4)
	print(c3)
	c3 = c1.sub2ComplexNo(c2)
	print(c3)
	'''
	
	
if __name__=="__main__":
	main()

'''
D:\F DATA\python_class>python oop_complex.py
13 + 10i
Destructing self 13 + 10i
14 + 8i
Destructing self 14 + 8i
7 + 6i
Destructing self 10 + 8i
Destructing self 3 + 2i
Destructing self 7 + 6i
'''

'''
D:\F DATA\python_class>python oop_complex.py
13 + 10i

14 + 8i

7 + 6i

6 + 8i

30 + 16i

True
False
True
False

True
'''