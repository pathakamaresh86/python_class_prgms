#!/usr/bin/python
#Nested function
def add_number(num):
	def adder(number):
		return num+number
	return adder

def main():
	addr_of_20=add_number(20) #adder reference : num set to 20
	print type(addr_of_20)
	print addr_of_20(10)
	
	addr_of_100=add_number(100) #adder reference : num set to 100
	print addr_of_100(10)

if __name__=="__main__":
	main()
	
'''
D:\F DATA\python_class>python function_closure.py
<type 'function'>
30
110
'''