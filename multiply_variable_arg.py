#!/usr/bin/python
#multiply any number of arguments

def multiply(*args):
    mult=1
    for x in args:
        mult=mult*x
    return mult
print multiply(10,20)
print multiply(10,20,30)
print multiply(10,20,30,40)
print multiply(10,20,30,40,50)