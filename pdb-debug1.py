#!/usr/bin/python
import pdb
class Test(object):
	def __init__(self, numberOfIteration):
		self.iterate=numberOfIteration
	def Display(self):
		for i in range(self.iterate):
			pdb.set_trace()
			print i
		return
		
if __name__ == '__main__':
	t = Test(5)
	t.Display()
	
'''
D:\F DATA\python_class>python pdb-debug1.py
> d:\f data\python_class\pdb-debug1.py(9)Display()
-> print i
(Pdb) n
0
> d:\f data\python_class\pdb-debug1.py(7)Display()
-> for i in range(self.iterate):
(Pdb) n
> d:\f data\python_class\pdb-debug1.py(8)Display()
-> pdb.set_trace()
(Pdb) n
> d:\f data\python_class\pdb-debug1.py(9)Display()
-> print i
(Pdb) n
1
> d:\f data\python_class\pdb-debug1.py(7)Display()
-> for i in range(self.iterate):
(Pdb) c
> d:\f data\python_class\pdb-debug1.py(9)Display()
-> print i
(Pdb) c
2
> d:\f data\python_class\pdb-debug1.py(8)Display()
-> pdb.set_trace()
(Pdb) c
3
> d:\f data\python_class\pdb-debug1.py(9)Display()
-> print i
(Pdb) c
4
'''