#!/usr/bin/python

def printStar1(no):
	for x in range(1,no+1):
		for _ in range(x):
			print '*\t',
		print

'''
def printStarOneLoop(no):
	temp=""
	for x in range(1,no+1):
		temp=temp + "*\t"
		print temp,
		print
'''   

def printStar2(no):
	for x in range(no,0,-1):
		for _ in range(x):
			print '*\t',
		print
	   
def printStar3(no):
	for x in range(1,no+1):
		for _ in range(no-x):
			print '\t',
		for _ in range(x):
			print '*\t',
		print
	   

def printStar4(no):
	for x in range(no,0,-1):
		for _ in range(no-x):
			print '\t',
		for _ in range(x):
			print '*\t',
		print
	   
	   
def main():
	no = input("Enter no of rows")
	printStar1(no)
	print "\n\n\n"
	printStar2(no)
	print "\n\n\n"
	printStar3(no)
	print "\n\n\n"
	printStar4(no)
	print "\n\n\n"
if __name__=="__main__":
	main()

