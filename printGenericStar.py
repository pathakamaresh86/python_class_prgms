#!/usr/bin/python

def printStar1(no,ch):
	for x in range(1,no+1):
		for _ in range(x):
			print ch +'\t',
		print
	   

def printStar2(no,ch):
	for x in range(no,0,-1):
		for _ in range(x):
			print ch + '\t',
		print
	   
def printStar3(no,ch):
	for x in range(1,no+1):
		for _ in range(no-x):
			print '\t',
		for _ in range(x):
			print ch +'\t',
		print
	   

def printStar4(no,ch):
	for x in range(no,0,-1):
		for _ in range(no-x):
			print '\t',
		for _ in range(x):
			print ch + '\t',
		print
	   
	   
def main():
	no = input("Enter no of rows")
	ch = input("Enter character")
	printStar1(no,ch)
	print "\n\n\n"
	printStar2(no,ch)
	print "\n\n\n"
	printStar3(no,ch)
	print "\n\n\n"
	printStar4(no,ch)
	print "\n\n\n"
if __name__=="__main__":
	main()

