#!/usr/bin/python

class AutoGenerate:
	def __init__(self,start,end,step=1):
		self.start=start
		self.end=end
		self.step=step
	
	def next(self):
		self.start+=self.step
		if self.start >= self.end:
			raise StopIteration
		return self.start
		
	#for 3.x
	def __next__(self):
		self.next()
	
	def __iter__(self):
		return self
		
def main():
	x = AutoGenerate(0, 100, 5)
	#for internally calls iter on obj, while wont do it so we need separate iter(x) 
	for y in x:
		print y
	'''
	z = iter(x)
	print(next(z))
	print(next(z))
	print(next(z))
	'''
	
if __name__ == "__main__":
	main()
	
'''
D:\F DATA\python_class>python iter_classObj.py
5
10
15
20
25
30
35
40
45
50
55
60
65
70
75
80
85
90
95
'''