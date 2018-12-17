#!/usr/bin/python

# Decorator functions apply only when an Object gets created as it requires an explicit calling to the wrapper function
def VerifyManagerMethods(cls):
	def wrapper():
		manager_init_method = False
		manager_del_method = False
		print cls.__dict__
		for key in cls.__dict__.iterkeys():
			if key == "__init__":
				manager_init_method = True
			elif key == "__del__":
				manager_del_method = True
		if not manager_init_method or not manager_del_method:
			raise NameError("constructor or destructor not found")
		else:
			print("Constructor & Destructor Found")
		return cls
	return wrapper
	
@VerifyManagerMethods
class Test2:
	def __init__(self):
		pass
	def __del__(self):
		pass

t2=Test2()		
#t2 = VerifyManagerMethods(Test2)
#t1=t2()

@VerifyManagerMethods
class Test:
	pass

t = Test()

'''
D:\F DATA\python_class>python decorator_metaclass.py
{'__del__': <function __del__ at 0x0000000002EF2DD8>, '__module__': '__main__', '__doc__': None, '__init__': <function __init__ at 0x0000000002EF2D68>}
Constructor & Destructor Found
{'__module__': '__main__', '__doc__': None}
Traceback (most recent call last):
  File "decorator_metaclass.py", line 34, in <module>
    t = Test()
  File "decorator_metaclass.py", line 15, in wrapper
    raise NameError("constructor or destructor not found")
NameError: constructor or destructor not found
'''