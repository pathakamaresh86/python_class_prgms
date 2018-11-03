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

def main():
    a=input("Enter no")
    if(prime(a)):
        print "is prime"
    else:
        print "not prime"

if __name__ == '__main__':
    main()
	
'''
D:\F DATA\python_class>python prime.py
Enter no12
not prime

D:\F DATA\python_class>python prime.py
Enter no121
not prime

D:\F DATA\python_class>python prime.py
Enter no11
is prime
'''