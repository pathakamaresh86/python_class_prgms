#!/usr/bin/python
#WAP to create dictionary of fibonacci series

		
def fibonacciDict(no):
	fib_dict={}
	n1 = 0
	n2 = 1
	fib_no=0
	if no <= 0:
		return {}
	if no == 1:
		fib_dict={1:1}
	else:
		fib_dict={1:1}
		cnt=2
		while cnt <= no:
			fib_no = n1 + n2
			fib_dict[cnt]=fib_no
			n1 = n2
			n2 = fib_no
			cnt=cnt+1
	return fib_dict
		
	   
def main():
	no=input("Enter number:")
	fib_dict=fibonacciDict(no)
	print "fibonacci dict",fib_dict
	
if __name__=="__main__":
	main()
	
'''
D:\F DATA\python_class>python ListFindFibonacciNo.py
Enter list of integers:[1,4,5,13,16,17,20,21]
fibonacci seq numbers in the list are [1, 5, 13, 21]
'''