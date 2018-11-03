#!/usr/bin/python
#Variable arguements
def VariableArgs(*args):
    print(type(args))
    for x in args:
        print x
		
VariableArgs()
VariableArgs(1)
VariableArgs(1,2,3,4)
VariableArgs(100,200,50,40,70,90,101)
VariableArgs(1,"Hello",2,[1,7,11],100)

'''
D:\F DATA\python_class>python variable_args.py
<type 'tuple'>
<type 'tuple'>
1
<type 'tuple'>
1
2
3
4
<type 'tuple'>
100
200
50
40
70
90
101
<type 'tuple'>
1
Hello
2
[1, 7, 11]
100
'''

def Add(a,b,*args):
    print type(a)
    print type(b)
    print type(args)
Add(1,2,3,4,5)	