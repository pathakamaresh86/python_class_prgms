#!/usr/bin/python

#static and class method decorators
class Test(object):

	#class method, when invoked using class name or class object take first arguement as reference to class
	
	@classmethod #c.Display()
	def Display(cls):
		print(id(cls))
		print("Display")

	@staticmethod	
	def Foo():
		print("Static Method")

	#Class - object method
	def InstanceDisplay(self):
		print("Instance Display")
		
c = Test()
c.InstanceDisplay()
Test.InstanceDisplay(c)

c.Foo()
Test.Foo()

c.Display()
Test.Display()

'''
D:\F DATA\python_class>python decorator_staticmethod_classmethod.py
Instance Display
Instance Display
Static Method
Static Method
30290680
Display
30290680
Display
'''