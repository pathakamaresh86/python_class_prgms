#!/usr/bin/python
'''
num1,num2=input("Enter two numbers")
print "Num1=", num1
print "Num2=", num2

if num1>num2 :
    print num1-num2
else :
    print num2-num1

num1,num2,num3=input("Enter three numbers")
print "Num1=", num1
print "Num2=", num2
print "Num3=", num3

#max 0f 3
if num1>num2 and num1>num3 :
    print str(num1) + "is greater"
elif num2>num3 :
    print str(num2) + "is greater"
else :
    print str(num3) + "is greater"

# min of 3
if num1<num2 and num1<num3 :
    print str(num1) + "is smaller"
elif num2<num3 :
    print str(num2) + "is smaller"
else :
    print str(num3) + "is smaller"
'''
#WAP to accept a no from user, if it is <=2 print "too few donuts" if it is between 3 to 10 then display "no of donuts:<value>", if greater than 10 then print "no of donuts too many"
num1=input("Enter number")
print "Num1=", num1
if num1 > 0:
    if num1 <=2 :
        print "Too few donuts"
    elif num1<=10 :
        print "no of donuts:" + str(num1)
    else:
        print "no of donuts too many"
else:
    print "Invalid no"
	
'''
D:\F DATA\python_class>python control_stmt.py
Enter two numbers10,11
Num1= 10
Num2= 11
1
Enter three numbers10,11,112
Num1= 10
Num2= 11
Num3= 112
112is greater
10is smaller
Enter number8
Num1= 8
no of donuts:8
'''