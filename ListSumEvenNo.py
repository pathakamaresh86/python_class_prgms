#!/usr/bin/python

def SumOfEvenNo(l1):
	sum=0
	for no in l1:
		if no&1 == 0:
			sum+=no
	return sum
			
def main():
	l1=input("enter list of integers:")
	sum = SumOfEvenNo(l1)
	print "Sum of even numbers in the list is",sum

if __name__ == "__main__":
    main()

'''
D:\F DATA\python_class>python ListSumEvenNo.py
enter list of integers:[1,2,3,4,5,6,7]
Sum of even numbers in the list is 12

D:\F DATA\python_class>python ListSumEvenNo.py
enter list of integers:[1,3,5]
Sum of even numbers in the list is 0
'''