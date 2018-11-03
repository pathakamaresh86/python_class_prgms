#!/usr/bin/python
#add any number of arguments

def add(*args):
    sum=0
    for x in args:
        sum=sum+x
    return sum
print add(10,20)
print add(10,20,30)
print add(10,20,30,40)
print add(10,20,30,40,50)