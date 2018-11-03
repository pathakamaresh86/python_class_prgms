#!/usr/bin/python
def Add(a,b):
    return a+b

#if we import module then it wont load below part	
if __name__ == '__main__':
    x,y=input("enter two no")
    print Add(x,y)
	
'''
D:\F DATA\python_class>python use__name__.py
enter two no1,2
3

>>> import use__name__
>>> use__name__.Add(100,200)
300
'''