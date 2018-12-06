#!/usr/bin/python
import re
def main():
	fd = open("re_mult.txt")
	data = fd.read()
	print data
	# starts with a but prints only one occurance even if multiline flag is true, as multiline needs ^ or $ 
	#for x in re.finditer("\Aa", data, re.MULTILINE | re.IGNORECASE):
	for x in re.finditer("^a", data, re.MULTILINE | re.IGNORECASE):
		print x.start(), x.end(), data[x.start():x.end()]
if __name__ == "__main__":
	main()
	
'''
D:\F DATA\python_class>python regex_multiline.py
abbs
aa AAasfdsf
dsfsdf
aa
AAdsfs
sfd

0 1 a

D:\F DATA\python_class>python regex_multiline.py
abbs
aa AAasfdsf
dsfsdf
aa
AAdsfs
sfd

0 1 a
5 6 a
24 25 a
27 28 A
'''