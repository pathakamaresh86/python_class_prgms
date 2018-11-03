#!/usr/bin/python


def IsDivisibleBy128(nnm1):
    result = num1&127
    if (result == 0):
        return True
    else:
        return False

num1=input("Enter number")
print "Entered number ", num1

'''bin(no) put it in str and check if last 7 are zero'''
if IsDivisibleBy128(num1):
    print str(num1) + " is divisible by 128"
else:
    print str(num1) + " is not divisible by 128"
	

def DecimalToBianry(l1):
    for x in l1:
        num=""
        while(x>0):
            num=num+str(x%2)
            x=x//2
        print num[::-1]
			
l1=[1890,32761,4810,7447,121340]
DecimalToBianry(l1)

def multipleOfFiveInRange(num1,num2):
    for x in range(num1,num2):
        if((x%5)==0):
	        print x

num1,num2=input("Enter lower bound number and upper bound number")
print "Entered numbers ", num1,num2
multipleOfFiveInRange(num1,num2)

'''
Output:
D:\F DATA\python_class>python day6_assign.py
Enter number128
Entered number  128
128 is divisible by 128
11101100010
111111111111001
1001011001010
1110100010111
11101100111111100
Enter lower bound number and upper bound number1,11
Entered numbers  1 11
5
10
'''