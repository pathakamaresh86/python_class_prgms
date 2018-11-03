#!/usr/bin/python
#WAP to accept 2 list from user sort them adn merge both list into third element by element,preserving sort order
def MergedList(l1,l2):
	len_l1=len(l1)
	len_l2=len(l2)
	j,i=0,0
	l3=[]
	while(i<len_l1 and j<len_l2):
		if l1[i]<l2[j]:
			l3.append(l1[i])
			i+=1
		else:
			l3.append(l2[j])
			j+=1
	if i<len_l1:
		l3.extend(l1[i:])
	if j<len_l2:
		l3.extend(l2[j:])
	return l3
	
def main():
	l1 = input("Enter list1: ")
	l2 = input("Enter list2:")
	l1.sort()
	l2.sort()
	MergeList=MergedList(l1,l2)
	print "Merged list is", MergeList
	

if __name__=="__main__":
	main()

'''
D:\F DATA\python_class>python List_Merge2Lists.py
Enter list1: [3,5,7,1,2]
Enter list2:[8,4,9]
Merged list is [1, 2, 3, 4, 5, 7, 8, 9]
'''