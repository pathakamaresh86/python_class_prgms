#!/usr/bin/python

def sqr(x):
	return x*x
	
x=lambda y: y*y
print x(3)

x=lambda y,z: y*z
print x(3,4)

x=lambda y,z: [y*z, y+z]
print x(3,4) 


'''
D:\F DATA\python_class>python lambda-ex.py
9
12
[12, 7]
'''