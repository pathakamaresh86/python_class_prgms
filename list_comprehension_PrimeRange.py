#!/usr/bin/python
def prime(a):
    if a > 2:
        if a == 3:
            return True
        if a%2 == 0:
            return False
        for x in range(3, int(a//2) + 2, 2): #int() typecast might need as '//' gives float no 1.0
            if(a%x == 0):
                return False
        else:		
            return True
    else:
        return False
		
def primeInRange(no1,no2):
	print [x for x in range(no1,no2) if prime(x) == True ]
	
		
def main():
	no1 = input("Enter start no")
	no2= input("Enter End no")
	primeInRange(no1,no2)

if __name__ == "__main__":
	main()
	
'''
D:\F DATA\python_class>python list_comprehension_PrimeRange.py
Enter start no1
Enter End no101
[3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
'''