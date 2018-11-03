#!/usr/bin/python

def ListOfNumDivBy8(l1):
	l2=set()
	for i in l1:
		if i & 7 == 0:
			l2.add(i)
	return l2
		
			
def main():
	l1=input("enter list1:")
	l2=ListOfNumDivBy8(l1)
	print l2

if __name__ == "__main__":
    main()

'''
D:\F DATA\python_class>python listNoDivisibleBy8.py
enter list1:[1,16,17,25,72,88]
set([16, 72, 88])
'''