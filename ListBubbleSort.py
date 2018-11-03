#!/usr/bin/python

#WAP to aceept list of numbers from user and sort them using bubble sort

def BubbleSort(l1):
	length = len(l1)
	i=0
	j=0
	while i < length:
		while j+1 < length -i:
			if l1[j]>l1[j+1]:
				temp=l1[j]
				l1[j]=l1[j+1]
				l1[j+1]=temp
			j+=1
		i+=1
	return l1
	
def main():
	l1 = input("Enter list of elements: ")
	l1=BubbleSort(l1)
	print "sorted list is", l1

if __name__=="__main__":
	main()
	
'''
D:\F DATA\python_class>python ListBubbleSort.py
Enter list of elements: [5,2,1,3]
sorted list is [2, 1, 3, 5]
'''