#!/usr/bin/python
def sub(a,b,c,d):
    return (a+b) - (c+d)

#Keyword arguements
#sub(10,20,d=100,30) '''error as it looks to align value for 4th parameter only'''
sub(10,20,d=100,c=30)

#default value
def slice(x,start,end,step=1):
    return x[start:end:step]
print slice("amaresh",3,5)


'''
#error:SyntaxError: non-default argument follows default argument
def slice(x,start,end=-1,step):
    return x[start:end:step]
print slice("amaresh",3,5)
'''
