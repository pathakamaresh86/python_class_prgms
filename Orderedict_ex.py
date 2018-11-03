#!/usr/bin/python
#Explore ordered dictionary, use existing module and use different functions
from collections import OrderedDict
def OrderedDictOpr():
	print("This is a Dict:\n") 
	d = {} 
	d['a'] = 1
	d['b'] = 2
	d['c'] = 3
	d['d'] = 4
  
	for key, value in d.items(): 
		print(key, value) 
  
	print("\nThis is an Ordered Dict:\n") 
	od = OrderedDict() 
	od['a'] = 1
	od['b'] = 2
	od['c'] = 3
	od['d'] = 4
  
	for key, value in od.items(): 
		print(key, value)
	
	print "Before changing:"
	for key, value in od.items(): 
		print(key, value)
	
	od['c']=5
	print "After changing:"
	for key, value in od.items(): 
		print(key, value)

	print("Before deleting:\n") 
	  
	for key, value in od.items(): 
		print(key, value) 
	  
	print("\nAfter deleting:\n") 
	od.pop('c') 
	for key, value in od.items(): 
		print(key, value) 
	  
	print("\nAfter re-inserting:\n") 
	od['c'] = 3
	for key, value in od.items(): 
		print(key, value) 


def main():
	OrderedDictOpr()
if __name__=="__main__":
	main()

'''
D:\F DATA\python_class>python Orderedict_ex.py
This is a Dict:

('a', 1)
('c', 3)
('b', 2)
('d', 4)

This is an Ordered Dict:

('a', 1)
('b', 2)
('c', 3)
('d', 4)
Before changing:
('a', 1)
('b', 2)
('c', 3)
('d', 4)
After changing:
('a', 1)
('b', 2)
('c', 5)
('d', 4)
Before deleting:

('a', 1)
('b', 2)
('c', 5)
('d', 4)

After deleting:

('a', 1)
('b', 2)
('d', 4)

After re-inserting:

('a', 1)
('b', 2)
('d', 4)
('c', 3)
'''