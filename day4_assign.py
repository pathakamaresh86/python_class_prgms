#!/usr/bin/python

str=input("Enter string")
print "Entered string ", str
print "first tow and last two char string ", str[1:3:1]+str[-1:-3:-1]


str1=input("Enter string")
print "Entered string ", str1
print "occurance replaced string", str1[:1]+str1[1:].replace("b", "*")

str1,str2=input("Enter two strings")
print "str1=", str1
print "str2=", str2
print "swapped first two character strings", str2[:2] + str1[2:], str1[:2] + str2[2:]

str1,str2=input("Enter two strings")
print "str1=", str1
print "str2=", str2
size1=len(str1)
size2=len(str2)
if size1 != size2:
    print "2nd string is not right rotation of 1st"
temp=str1+str1
#if (temp.count(str2)> 0):
if (str2 in temp):
    print "2nd string is right rotation of 1st"
else:
    print "2nd string is not right rotation of 1st"
	
str1=input("Enter string")
print "Entered string ", str1
str2="not bad"
if (str2 in str1):
    print str1.replace("not bad", "good")
else:
    print "string not contain not bad"




