#!/usr/bin/python

#WAP to aceept list of numbers from user and sort them using bubble sort

def SelectionSort(l1):
	length = len(l1)
	i=0
	j=0
	while i < length:
		min_idx = i
		j=i+1
		while j < length:
			if l1[min_idx]>l1[j]:
				min_idx=j
			j+=1
		temp=l1[min_idx]
		l1[min_idx]=l1[i]
		l1[i]=temp
		i+=1
	return l1
	
def main():
	l1 = input("Enter list of elements: ")
	l1=SelectionSort(l1)
	print "sorted list is", l1

if __name__=="__main__":
	main()
	
'''
D:\F DATA\python_class>python ListBubbleSort.py
Enter list of elements: [5,2,1,3]
sorted list is [2, 1, 3, 5]
'''