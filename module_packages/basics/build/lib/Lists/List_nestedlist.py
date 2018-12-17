#!/usr/bin/python
#WAP to accept nested list and print individual element as list 
def normalize_list(l1,result=[]):
	i=0
	while i<len(l1):
		if type(l1[i])!=list:
			result.append(l1[i])
		else:
			normalize_list(l1[i],result)
		i+=1
	
def main():
	result=[]
	l1 = input("Enter nested list1: ")
	normalize_list(l1,result)
	print result
	

if __name__=="__main__":
	main()

'''
D:\F DATA\python_class>python List_nestedlist.py
Enter nested list1: [1,2,[3,4,[5,6]],7,[8,9],10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''