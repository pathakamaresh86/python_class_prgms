#!/usr/bin/python

def Add2Numbers(self):
	return self.no1 + self.no2

def Mul(self):
	return self.no1 * self.no2
	
def init(self, a, b):
	self.no1 = a
	self.no2 = b
	
def main():
	Arithmetic = type('Arithmetic',(object,),{'__init__':init, 'Adding':Add2Numbers, 'Mul':Mul})
	obj = Arithmetic(10,20)
	print Arithmetic.__dict__
	print obj.Adding()
	print obj.Mul()
	
if __name__ == "__main__":
	main()
'''
D:\F DATA\python_class>python meta_class_CreateClass.py
{'Adding': <function Add2Numbers at 0x00000000033CBC88>, '__module__': '__main__', '__dict__': <attribute '__dict__' of 'Arithmetic' objects>, 'Mul': <function Mul at 0x00000000033CBCF8>, '__weakref__': <attribute '__weakref__' of 'Arithmetic' objects>, '__doc__': None, '__init__': <function init at 0x00000000033CBD68>}
30
200
'''