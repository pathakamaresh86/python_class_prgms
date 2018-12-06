class A(object):
	def m(self):
		print("A's M")

class B(A):
	def l(self):
		print("B's L")

class C(A):
	def m(self):
		print("C's M")
		

class D(B,C):
	pass

def main():
	a=A()
	a.m()
	b=B()
	b.l()
	c=C()
	c.m()
	d=D()
	d.m()

if __name__ == "__main__":
	main()
	
'''
#Not inheriting A from object
D:\F DATA\python_class>python oop_diamondPrblm.py
A's M
B's L
C's M
A's M

#After inheriting A from object
D:\F DATA\python_class>python oop_diamondPrblm.py
A's M
B's L
C's M
C's M
