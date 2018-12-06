#!/usr/bin/python
import re

def validateIP(ip_addr):
	'''
	x=re.match("(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})","10.100.200.200")
	>>> print x.group(1)
	10
	>>> print x.groups()
	('10', '100', '200', '200')
	'''
	x=re.match("(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})",ip_addr)
	flag=0
	if x == None:
		print "Ip address format is wrong"
	else: 
		if int(x.group(1)) in range (1,256):
			if int(x.group(2)) not in range (0,256):
				print "Invalid ip address"
			else:
				if int(x.group(3)) not in range (0,256):
					print "Invalid ip address"
				else:
					if int(x.group(4)) not in range (0,256):
						print "Invalid ip address"
					else:
						print "Correct Ip address entered"
						flag=1
		else:
			print "Invalid ip address"          
				
	if flag == 1:
		if int(x.group(1)) in range (0,127):
			print str(ip_addr), " is belongs to Class A"
		
		elif int(x.group(1)) in range (128,192):
			print str(ip_addr), " is belongs to Class B"
		
		elif int(x.group(1)) in range (192,224):
			print str(ip_addr), " is belongs to Class C"
		
		elif int(x.group(1)) in range (224,240):
			print str(ip_addr), " is belongs to Class D"
			
		elif int(x.group(1)) in range (240,256):
			print str(ip_addr), " is belongs to Class E"
	
def main():
	ip_addr=input("Enter ip address in string ")
	validateIP(ip_addr)


if __name__ == "__main__":
	main()

'''
D:\F DATA\python_class>python regex_validateip.py
Enter ip address in string "10.20.30.40"
Correct Ip address entered

D:\F DATA\python_class>python regex_validateip.py
Enter ip address in string "0.20.30.40"
Invalid ip address

D:\F DATA\python_class>python regex_validateip.py
Enter ip address in string "10.300.30.40"
Invalid ip address

D:\F DATA\python_class>python regex_validateip.py
Enter ip address in string "10.20.300.40"
Invalid ip address

D:\F DATA\python_class>python regex_validateip.py
Enter ip address in string "10.20.30.256"
Invalid ip address

D:\F DATA\python_class>python regex_validateip.py
Enter ip address in string "10.20.30.40"
Correct Ip address entered

D:\F DATA\python_class>python regex_validateip.py
Enter ip address in string "10.20.30.40"
Correct Ip address entered

D:\F DATA\python_class>python regex_validateip.py
Enter ip address in string "10.20.30.40"
Correct Ip address entered
10.20.30.40  is belongs to Class A

D:\F DATA\python_class>python regex_validateip.py
Enter ip address in string "128.20.30.40"
Correct Ip address entered
128.20.30.40  is belongs to Class B

D:\F DATA\python_class>python regex_validateip.py
Enter ip address in string "192.20.30.40"
Correct Ip address entered
192.20.30.40  is belongs to Class C

D:\F DATA\python_class>python regex_validateip.py
Enter ip address in string "200.20.30.40"
Correct Ip address entered
200.20.30.40  is belongs to Class C

D:\F DATA\python_class>python regex_validateip.py
Enter ip address in string "224.20.30.40"
Correct Ip address entered
224.20.30.40  is belongs to Class D

D:\F DATA\python_class>python regex_validateip.py
Enter ip address in string "240.20.30.40"
Correct Ip address entered
240.20.30.40  is belongs to Class E
'''