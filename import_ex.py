#!/usr/bin/python
def Add(a,b):
    return a+b

def main():
    x,y=input("Enter two no")
    print("Result of x+y=%d" %Add(x,y))

if __name__ == '__main__':
    print ("Running as standalone script",__name__)
    main()
else:
    print ("Loaded as module",__name__)
	
'''
D:\F DATA\python_class>python import_ex.py
('Running as standalone script', '__main__')
Enter two no2,3
Result of x+y=5

D:\F DATA\python_class>python
Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import import_ex
('Loaded as module', 'import_ex')
>>> import_ex.Add(3,4)
7

Change Add function
>>> import import_ex
>>> import_ex.Add(3,4) #it wont reflected
7


D:\F DATA\python_class>python
Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import import_ex
('Loaded as module', 'import_ex')
>>> import_ex.Add(3,4)
-1
>>>

D:\F DATA\python_class>python
Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from import_ex import *
('Loaded as module', 'import_ex')
>>> Add(5,4)
1
>>> main()
Enter two no2,3
Result of x+y=-1


D:\F DATA\python_class>python
Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import import_ex as ui
('Loaded as module', 'import_ex')
>>> ui.Add(2,3)
5
'''