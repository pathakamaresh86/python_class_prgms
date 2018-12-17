#!/usr/bin/python

import time
def LogDecorator(func):
	print "Invokes LogDecorator at loading"
	#name of init cna be different
	def log(args):
		return func(str(time.time()) + "  "+args)
	return log
	
def NameDecorator(func):
	print "Invokes NameDecorator at loading"
	#name of init cna be different
	def log(args):
		return func("Test Solution: " + args)
	return log

@LogDecorator
@NameDecorator
def Logger(data):
	print("Logger {}".format(data))
	
def main():
	#By using decorator
	Logger("Top")
	time.sleep(1)
	Logger("PS")	
	
if __name__=="__main__":
	main()
	
'''
D:\F DATA\python_class>python decorator_chaining.py
Invokes NameDecorator at loading
Invokes LogDecorator at loading
Logger Test Solution: 1544335019.1  Top
Logger Test Solution: 1544335020.1  PS
'''