#!/usr/bin/python

def pattern1234(no):
	for i in range(1,no+1):
		k=0+i
		for _ in range(no-i):
			print "\t",
		for l in range(1,2*i):
			print str(k) + '\t',
			if l < i:
				k=k-1
			else:
				k=k+1
		print
		
def main():
	no = input("Enter no of rows")
	pattern1234(no)
if __name__=="__main__":
	main()

'''
D:\F DATA\python_class>python pattern1234.py
Enter no of rows5
                                1
                        2       1       2
                3       2       1       2       3
        4       3       2       1       2       3       4
5       4       3       2       1       2       3       4       5

'''