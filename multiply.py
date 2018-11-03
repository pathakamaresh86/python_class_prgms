#!/usr/bin/python
#Write a single function to multiply 2,3,4,5 numbers.
def multiply(a,b,c=1,d=1,e=1):
    return (a*b*c*d*e)
print multiply(1,2)
print multiply(1,2,3)
print multiply(1,2,3,4)
print multiply(1,2,3,4,5)

'''
D:\F DATA\python_class>python multiply.py
2
6
24
120
'''