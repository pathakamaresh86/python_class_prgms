#!/usr/bin/python
#WAP to print list elements one by one and print their type 
def listElemType(l1):
	for elem in l1:
		print elem,type(elem)
	
def main():
	l1 = input("Enter list1: ")
	listElemType(l1)
	

if __name__=="__main__":
	main()

'''
D:\F DATA\python_class>python List_element_type.py
Enter list1: [1,"abc",[1,2,3],{1:2,3:4}]
1 <type 'int'>
abc <type 'str'>
[1, 2, 3] <type 'list'>
{1: 2, 3: 4} <type 'dict'>
'''