#!/usr/bin/python

class ReferenceCount1:
	def __init__(self, start):
		self.start = start
	
	#Forward Iterator
	#Here __iter__ is using yield so iter() is not required hence __iter__ is not returning obj and next method is not writen
	def __iter__(self):
		start = self.start
		while start > 0:
			yield start
			start -= 1
	
	def __reversed__(self):
		start = 1
		while start <= self.start:
			yield start
			start += 1

def main():
	x = ReferenceCount1(10)
	print("Display from 10---1")
	for y in x:
		print (y)
	
	print("Display from 1---10")
	for w in reversed(x):
		print(w)
		
if __name__ == "__main__":
	main()

'''
D:\F DATA\python_class>python iter_reverse.py
Display from 10---1
10
9
8
7
6
5
4
3
2
1
Display from 1---10
1
2
3
4
5
6
7
8
9
10
'''