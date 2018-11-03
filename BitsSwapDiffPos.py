#!/usr/bin/python

def SwapBitsDiffPos(no1,no2,pos1,pos2,bits):
	x = (1<<bits) -1
	y = x << (pos1 - bits)
	z = x << (pos2 - bits)
	no1_part = no1 & y
	no2_part = no2 & z
	no1 = no1 & ~y
	no2 = no2 & ~z
	no1 = no1 | no2_part
	no2 = no2 | no1_part
	return no1,no2


def main():
	no1 = input("Enter number1: ")
	no2 = input("Enter number2: ")
	pos1 = input("Enter position1: ")
	pos2 = input("Enter position2: ")
	bits = input("Enter bits: ")
	print "Original numbers",no1, no2
	no1,no2 = SwapBitsDiffPos(no1,no2,pos1,pos2,bits)
	print "Number after swapping the bits", no1, no2
	
	
if __name__=="__main__":
	main()
	
'''
D:\F DATA\python_class>python BitsSwapDiffPos.py
Enter number1: 102
Enter number2: 105
Enter position1: 5
Enter position2: 6
Enter bits: 4
Original numbers 102 105
Number after swapping the bits 104 71
'''