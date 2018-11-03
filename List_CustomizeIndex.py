#!/usr/bin/python
#WAP to customize index function which returns list of indices where the given data is present in input list
def custIndex(l1,searchNo):
	count = 0
	result=[]
	
	for x in l1:
		if x == searchNo:
			result.append(count)
		count = count + 1
	return result
		
def CustmizedAllIndices(l1,searchNo):
	result=[]
	count=l1.count(searchNo)
	prev_index = 0
	while count!=0:
		cur_index = l1[prev_index:].index(searchNo)
		result.append(cur_index + prev_index)
		count = count - 1
		prev_index = cur_index + 1 + prev_index
	return result
	
	
def main():
	result=[]
	result1=[]
	l1 = input("Enter list of elements: ")
	searchNo = input("Enter number to be searched:")
	result=custIndex(l1,searchNo)
	print "reulted Indices list is", result
	result1=CustmizedAllIndices(l1,searchNo)
	print "reulted Indices list is", result1
	

if __name__=="__main__":
	main()

'''
D:\F DATA\python_class>python List_CustomizeIndex.py
Enter list of elements: [1,2,3,2,4,5,2]
Enter number to be searched:2
reulted Indices list is [1, 3, 6]
reulted Indices list is [1, 3, 6]
'''