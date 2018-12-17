#!/usr/bin/python

def from_keys(x,value=None):
	i=0
	result=dict()
	if type(value) == int or type(value) == str:
		for key in x.keys():
			result[key]=value
	elif type(value) == list:
			for key in x.keys():
				if i<len(value):
					result[key]=value[i]
					i=i+1
				else:
					result[key]=None
	return result
				
def main():
	x=input("enter dictinary:")
	val=input("Enter value:")
	result=from_keys(x,val)
	print result

if __name__ == "__main__":
    main()

'''
D:\F DATA\python_class>python Dict_from_keys.py
enter dictinary:{1:1,2:2,3:3}
Enter value:[4,5,6]
{1: 4, 2: 5, 3: 6}

D:\F DATA\python_class>python Dict_from_keys.py
enter dictinary:{1:1,2:2,3:3}
Enter value:[4,5]
{1: 4, 2: 5, 3: None}

D:\F DATA\python_class>python Dict_from_keys.py
enter dictinary:{1:1,2:2,3:3}
Enter value:[4,5,6,7]
{1: 4, 2: 5, 3: 6}
'''
