#!/usr/bin/python
#WAP to accept list and find numbers which appears in fibbonacci seq

def fibonaccinList(l1):
	fib_list=[]
	for no in l1:
		l2=fibonacci_series(no)
		if l2.__contains__(no):
			fib_list.append(no)
	return fib_list
		
def fibonacci_series(no):
	n1 = 0
	n2 = 1
	fib_no=0
	l2=[]
	if no == 1:
		l2.append(no)
	else:
		l2.append(n1)
		while fib_no <= no:
			fib_no = n1 + n2
			l2.append(fib_no)
			n1 = n2
			n2 = fib_no
	return l2
		
	   
def main():
	l1=input("Enter list of integers:")
	fib_list=fibonaccinList(l1)
	print "fibonacci seq numbers in the list are",fib_list
	
if __name__=="__main__":
	main()
	
'''
D:\F DATA\python_class>python ListFindFibonacciNo.py
Enter list of integers:[1,4,5,13,16,17,20,21]
fibonacci seq numbers in the list are [1, 5, 13, 21]
'''