#!/usr/bin/python

def generator(x):
	return lambda n:n+x
	
generator_of_5=generator(5)
print generator_of_5(10)

generator_of_10=generator(10)
print generator_of_10(10)

'''
D:\F DATA\python_class>python lambda-generator.py
15
20
'''