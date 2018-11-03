#!/usr/bin/python
#Write a single function to add 2,3,4,5 numbers.
def add(a,b,c=0,d=0,e=0):
    return (a+b+c+d+e)
print add(10,20)
print add(10,20,30)
print add(10,20,30,40)
print add(10,20,30,40,50)

'''
D:\F DATA\python_class>python add.py
30
60
100
150
'''