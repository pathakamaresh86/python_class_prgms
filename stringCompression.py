#!/usr/bin/python
#WAP to accept string from user and print compression of it 
def stringCompress(str1):
	i=0
	cmpstr=''
	x=''
	while(i< len(str1)):
		cnt=1
		x=str1[i]
		while((i+1 < len(str1)) and (x==str1[i+1])):
			cnt = cnt+1
			i=i+1
		cmpstr += x+str(cnt)
		i=i+1
	return cmpstr
	
def main():
	str1 = input("Enter string")
	cmpstr=stringCompress(str1)
	print "Compress String ",cmpstr
if __name__=="__main__":
	main()

'''
D:\F DATA\python_class>python stringCompression.py
Enter string"abcd"
Compress String  a1b1c1d1

D:\F DATA\python_class>python stringCompression.py
Enter string"aaabbccaaadde"
Compress String  a3b2c2a3d2e1
'''