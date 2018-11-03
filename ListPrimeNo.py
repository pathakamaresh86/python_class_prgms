#!/usr/bin/python

def PrimeInList(l1):
	primeList=[]
	num=0
	x=0
	for num in l1:
		if num%2 == 0:
			continue
		for x in range(3, int(num//2) + 2, 1):
			if num%x == 0:
				break
		else:
			primeList.append(num)
	return primeList

def main():
	l1=input("Enter list of integers:")
	primeList=PrimeInList(l1)
	print "prime numbers in the list are",primeList

if __name__ == "__main__":
    main()

'''
D:\F DATA\python_class>python ListPrimeNo.py
Enter list of integers:[2,3,5,7,4,9,11]
prime numbers in the list are [3, 5, 7, 11]
'''