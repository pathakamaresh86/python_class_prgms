#!/usr/bin/python

def fibonacci_series(no):
	n1 = 0
	n2 = 1
	fib_no=0
	if no <= 0:
		print("Please enter a positive integer")
	elif no == 1:
		print "Fibonacci sequence",no
	else:
		print("Fibonacci sequence:")
		while fib_no <= no:
			print n1
			fib_no = n1 + n2
			n1 = n2
			n2 = fib_no
		
	   
def main():
	no = input("Enter a number: ")
	result01 = fibonacci_series(no)
	
if __name__=="__main__":
	main()