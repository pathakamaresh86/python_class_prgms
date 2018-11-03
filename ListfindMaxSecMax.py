#!/usr/bin/python
#WAP to find max and second max element from given list
def findMaxSecMax(l1):

	max = 0
	sec_max=0
	if l1 == None:
		return
	elif len(l1)==1:
		return l1[0],None
	else:
		max = l1[0]
		sec_max=l1[1]
		if sec_max > max:
			max=l1[1]
			sec_max=l1[0]
	for x in l1[2:]:
		if x > max:
			sec_max = max
			max = x
		elif x > sec_max:
			sec_max =x
	return max,sec_max
	
def main():
	l1 = input("Enter list of elements: ")
	max,sec_max=findMaxSecMax(l1)
	print "max number is", max
	print "second max number is", sec_max

if __name__=="__main__":
	main()
	
'''
D:\F DATA\python_class>python ListfindMaxSecMax.py
Enter list of elements: [1,2,3,3]
max number is 3
second max number is 3
'''