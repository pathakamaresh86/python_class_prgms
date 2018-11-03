#!/usr/bin/python

def Dict_Dict1keys_Dict2Val(x,y):
	i=0
	result=dict()
	valList = list()
	for val in y.values():
		valList.append(val)
	for key in x.keys():
		if i<len(valList):
			result[key]=valList[i]
			i=i+1
		else:
			result[key]=None
	return result
				
def main():
	x=input("enter dictinary1:")
	y=input("enter dictinary2:")
	result=Dict_Dict1keys_Dict2Val(x,y)
	print result

if __name__ == "__main__":
    main()

'''
D:\F DATA\python_class>python dict_keyDict1_valDict2.py
enter dictinary1:{1:1,2:2,3:3}
enter dictinary2:{5:5,6:[8,9,7],10:10}
{1: 10, 2: 5, 3: [8, 9, 7]}

D:\F DATA\python_class>python dict_keyDict1_valDict2.py
enter dictinary1:{1:1,2:2,3:3}
enter dictinary2:{5:5,6:[8,9,7]}
{1: 5, 2: [8, 9, 7], 3: None}

D:\F DATA\python_class>python dict_keyDict1_valDict2.py
enter dictinary1:{1:1,2:2,3:3}
enter dictinary2:{5:5,6:[8,9,7],10:10,11:11}
{1: 10, 2: 11, 3: 5}
'''
