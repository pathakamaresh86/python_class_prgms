#!/usr/bin/python

def printStar2(no):
	k="*\t"
	space_ch = "\t" 
	cols=(no+(no-1))
	for i in range(1,no+1):
		for _ in range(i):
			print k,
		for _ in range(cols-2*i):
			print space_ch,
		for l in range(i):
			if l != no-1:
				print k,
		print
		

def printStar3(no):
	k="*\t"
	space_ch = "\t" 
	cols=(no+(no-1))
	for i in range(no,0,-1):
		for _ in range(i):
			print k,
		for _ in range(cols-2*i):
			print space_ch,
		for l in range(i):
			if l != no-1:
				print k,
		print

def printStar4(no):
	cols=no+(no-1)
	k="*"
	for i in range(1,no+1):
		for _ in range(no-i):
			print "\t",
		for _ in range(1,2*i):
			print k + '\t',
		print
		cnt=1
	for j in range (no-1,0,-1):
		for _ in range(no-j):
			print "\t",
		for _ in range(2*j-1):
			print k + '\t',
			cnt+=1
		print
			
		
def main():
	no = input("Enter no of rows")
	#printStar2(no)
	#print
	#print
	#printStar3(no)
	printStar4(no)
if __name__=="__main__":
	main()

	
'''
*				*
*	*		*	*
*	*	*	*	*
'''