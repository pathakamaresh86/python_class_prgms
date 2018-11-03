#!/usr/bin/python

num1=input("Enter number")
print "Entered number ", num1

# if LSB(last bit) is zero then even if 1 then odd  
if num1&1 == 0:
    print str(num1) + " is even number"
else:
    print str(num1) + " is odd number"

num1=input("Enter number")
print "Entered number ", num1

if num1&15 == 0:
    print str(num1) + " is divisible by 16"
else:
    print str(num1) + " is not divisible by 16"
	
num1,num2,num3=input("Enter lenght of three sides of triangle")
print "Entered side1", num1
print "Entered side2", num2
print "Entered side3", num3

if num1>num2 and num1>num3 :
    side3=num1
    temp=num2 + num3
elif num2>num3 :
    side3=num2
    temp=num1 + num3
else :
    side3=num3
    temp=num1 + num2
	
if temp > side3:
    print "It is triangle"
else:
    print "not triangle"	

'''
D:\F DATA\python_class>python day5_assign.py
Enter number12
Entered number  12
12 is even number
Enter number144
Entered number  144
144 is divisible by 16
Enter lenght of three sides of triangle5,6,7
Entered side1 5
Entered side2 6
Entered side3 7
It is triangle
'''