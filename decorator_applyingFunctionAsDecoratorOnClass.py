#!/usr/bin/python

#Class attribute, Object attribute
#Dynamic classes 
def DecoratorClass(cls):
	cls.added_attribute="Decorated Attribute"
	cls.empty_list = []
	return cls
	
@DecoratorClass
class Temp(object):
	def __init__(self):
		self.acct_no = 1
	def Display(self):
		pass
		
@DecoratorClass
class Test(object):
	def __init__(self):
		self.id = 1

#Decorator method appy on class, not on object so t.__dict wont print decorator method variables
print Temp.__dict__
print Test.__dict__
t = Temp()
print t.__dict__

'''
D:\F DATA\python_class>python decorator_applyingFunctionAsDecoratorOnClass.py
{'added_attribute': 'Decorated Attribute', '__module__': '__main__', '__doc__': None, 'empty_list': [], '__dict__': <attribute '__dict__' of 'Temp' objects>, '__weakref__': <attribute '__weakref__' of 'Temp' objects>, 'Display': <function Display at 0x0000000003588DD8>, '__init__': <function __init__ at 0x0000000003588D68>}

{'added_attribute': 'Decorated Attribute', '__module__': '__main__', 'empty_list': [], '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None, '__init__': <function __init__ at 0x0000000003588E48>}

{'acct_no': 1}
'''