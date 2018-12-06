#!/usr/bin/python

def main():
	try:
		num = input("Enter numerator")
		denom = input("Enter denomenator")
		result = num/denom
		print result
	except ZeroDivisionError as e:
		print e
	except Exception as e:
		print "exception",e
	else:
		print "executes if no exception"
	finally:
		print "Execute always!!!"
	


if __name__ == "__main__":
	main()

'''
D:\F DATA\python_class>python exception_handling1.py
Enter numerator10
Enter denomenator0
integer division or modulo by zero
Execute always!!!

D:\F DATA\python_class>python exception_handling1.py
Enter numerator10
Enter denomenator2
5
executes if no exception
Execute always!!!

'''