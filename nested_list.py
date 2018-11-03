#!/usr/bin/python

def normalize_list(l1,result=[]):
	i=0
	while i<len(l1):
		if type(l1[i])!=list:
			result.append(l1[i])
		else:
			normalize_list(l1[i],result)
		i+=1
			
def main():
	l1=[]
	result=[]
	l1=input("enter list:")
	normalize_list(l1,result)
	print "nested list",result

if __name__ == "__main__":
    main()

'''
D:\F DATA\python_class>python nested_list.py
enter list:[1,2,3,[4,5,6,[7,8]],11,12]
nested list [1, 2, 3, 4, 5, 6, 7, 8, 11, 12]
'''