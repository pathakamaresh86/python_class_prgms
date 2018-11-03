#!/usr/bin/python

def CheckList2PartOf1(l1,l2):
	l1=set(l1)
	l2=set(l2)
	return l2.issubset(l1)
			
def main():
	l1=input("enter list1:")
	l2=input("enter list2:")
	print CheckList2PartOf1(l1,l2)

if __name__ == "__main__":
    main()

