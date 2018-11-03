#!/usr/bin/python

def SwapBits(no1,no2,pos,bits):
	x = (1<<bits) -1
	x = x << (pos - bits)
	no1_part = no1 & x
	no2_part = no2 & x
	no1 = no1 & ~x
	no2 = no2 & ~x 
	no1 = no1 | no2_part
	no2 = no2 | no1_part
	return no1,no2


def main():
	no1 = input("Enter number1: ")
	no2 = input("Enter number2: ")
	pos = input("Enter position: ")
	bits = input("Enter bits: ")
	print "Original numbers",no1, no2
	no1,no2 = SwapBits(no1,no2,pos,bits)
	print "Number after swapping the bits", no1, no2
	
	
if __name__=="__main__":
	main()
	
'''
D:\F DATA\python_class>python BitsSwap.py
Enter number1: 102
Enter number2: 105
Enter position: 5
Enter bits: 4
Original numbers 102 105
Number after swapping the bits 104 103
'''