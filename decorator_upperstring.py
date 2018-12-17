#!/usr/bin/python

def WrapperUpper(func):
	print "Invokes Wrapper at loading"
	#name of init cna be different
	def init():
		gen = func()
		next(gen)
		return gen
	return init

@WrapperUpper
def toUpper():
	while True:
		string = yield #data came from send method
		print string.upper()
		
	
if __name__=="__main__":
	#By using decorator
	y = toUpper() # consume calls inner function init 
	y.send("hello amaresh")

'''
D:\F DATA\python_class>python decorator_upperstring.py
Invokes Wrapper at loading
HELLO AMARESH
'''