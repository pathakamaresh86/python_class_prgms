#!/usr/bin/python
#multiply any number of arguments

def VariableDictionary(*args,**kwargs):
    print(type(args))
    print(type(kwargs))
    for x in args:
        print(x)
    print("Displaying dictionary keyword args variable length")
    for x in kwargs:
        print(x,kwargs[x])
		
result=VariableDictionary(1,2,name="amaresh",hobby="travel",Age=31)
print result #if function returns nothing it prints none

'''
D:\F DATA\python_class>python variable_dictionary.py
<type 'tuple'>
<type 'dict'>
1
2
Displaying dictionary keyword args variable length
('hobby', 'travel')
('Age', 31)
('name', 'amaresh')
none
'''