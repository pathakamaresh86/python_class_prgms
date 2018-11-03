#!/usr/bin/python
def sumDigits(no):
	if no in range(0,10):
		return no
	else:
		sum=0
		while(no>=1):
			sum= sum + (no%10)
			no=no//10
		return sum

def sumOddEvenDigits(no):
	sumEven=0
	sumOdd=0
	while(no>=1):
		rem = no%10 
		if rem%2==0:
			sumEven= sumEven + rem
		else:
			sumOdd = sumOdd + rem
		no=no//10
	print "Even digits sum: ", sumEven
	print "Odd digits sum: ", sumOdd
	print "Even digits sum - Odd digits sum: ", sumEven-sumOdd

def reverseDigits(no):
	if no in range(0,10):
		return no
	else:
		rev_no=0
		while(no>=1):
			rem = no%10
			rev_no= rev_no*10 + rem
			no=no//10
		return rev_no

def isPalindrom(no):
	rev_no = reverseDigits(no)
	if no == rev_no:
		return True
	return False

def isAmstrong(no):
	sumofcubes=0
	origno=no
	while(no>=1):
		rem = no%10
		sumofcubes = sumofcubes + rem**3
		no=no//10
	if origno == sumofcubes:
		return True
	return False

def main():
	no = input("Enter a number: ")
	result01 = sumDigits(no)
	print "Sum of digits",result01
	sumOddEvenDigits(no)
	print "reverse no= ",reverseDigits(no)
	if isPalindrom(no):
		print no," is palindrom"
	else:
		print no, " is not palindrom"
		
	if isAmstrong(no):
		print no," is amstrong"
	else:
		print no, " is not amstrong"
	
if __name__=="__main__":
	main()

'''
D:\F DATA\python_class>python digits_sum.py
Enter a number: 123
Sum of digits 6
'''