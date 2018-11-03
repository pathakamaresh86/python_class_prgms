#!/usr/bin/python

def printABCD1(no):
	for i in range(no,0,-1):
		k=64+i
		for _ in range(no-i):
			print "\t",
		for l in range(1,2*i):
			print chr(k) + '\t',
			if l < i:
				k=k-1
			else:
				k=k+1
		print
		
def main():
	no = input("Enter no of rows")
	printABCD1(no)
if __name__=="__main__":
	main()

'''
D:\F DATA\python_class>patternABCD1.py
Enter no of rows4
D       C       B       A       B       C       D
        C       B       A       B       C
                B       A       B
                        A
'''