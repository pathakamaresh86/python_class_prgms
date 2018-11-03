#!/usr/bin/python

def TurnoffBits(no,pos,bits):
	x = (1<<bits) -1
	x = x << (pos - bits)
	x = ~x
	return no & x

def TurnonBits(no,pos,bits):
	x = (1<<bits) -1
	x = x << (pos - bits)
	return no | x

def ToggleBits(no,pos,bits):
	x = (1<<bits) -1
	x = x << (pos - bits)
	return no ^ x
	   
def main():
	no = input("Enter a number: ")
	pos = input("Enter position: ")
	bits = input("Enter bits: ")
	
	result = TurnoffBits(no,pos,bits)
	print "Original number",no
	print "Number after turn off the bits", result
	
	result = TurnonBits(no,pos,bits)
	print "Original number",no
	print "Number after turn on the bits", result
	
	result = ToggleBits(no,pos,bits)
	print "Original number",no
	print "Number after turn on the bits", result
	
if __name__=="__main__":
	main()
	
'''
D:\F DATA\python_class>python BitsOpr.py
Enter a number: 102
Enter position: 4
Enter bits: 3
Original number 102
Number after turn off the bits 96
Original number 102
Number after turn on the bits 110
Original number 102
Number after turn on the bits 104
'''