#!/usr/bin/python
#WAP to accept no from user and create a dictionary of bit possition and corresponding value at that possition assuming 32 bit integer and consider lsb as starting position
def DecimalToBianry(no):
	bindict={}
	cnt=1
	while(no>0):
		bindict[cnt]=no%2
		no=no//2
		cnt = cnt + 1
	return bindict


def main():
	no=input("Enter Number:")
	bindict = DecimalToBianry(no)
if __name__=="__main__":
	main()
	
'''
D:\F DATA\python_class>python DictBinary.py
Enter Number:65
{1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 1}
'''