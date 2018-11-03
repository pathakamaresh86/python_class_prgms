#!/usr/bin/python
def digits(no):
	if no in range(0,10):
		return no
	else:
		temp=""
		while(no>=1):
			temp=temp + str(no%10)
			no=no//10
		return temp

def main():
	no = input("Enter a number: ")
	result01 = digits(no)
	print "digits in no",result01
	
if __name__=="__main__":
	main()

'''
D:\F DATA\python_class>python digits_of_no.py
Enter a number: 12
digits in no 21
'''