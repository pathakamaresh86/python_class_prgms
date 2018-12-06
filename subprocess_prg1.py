#!/usr/bin/python
import subprocess
import time
def execCmd(m,n):
	cnt=0
	while cnt < n:
		x=subprocess.check_output("dir D:\\bkp", shell=True)
		print x
		cnt +=1
		time.sleep(m)

def main():
	m=input("Enter delay time: ")
	n=input("Enter no of times to execute: ")
	execCmd(m,n)

if __name__ == "__main__":
	main()
	
'''
D:\F DATA\python_class>python subprocess_prg1.py
Enter delay time: 3
Enter no of times to execute: 3
 Volume in drive D is DATA
 Volume Serial Number is 6648-288E

 Directory of D:\bkp

09/26/2018  12:38 PM    <DIR>          .
09/26/2018  12:38 PM    <DIR>          ..
09/25/2018  01:47 PM    <DIR>          General_data
               0 File(s)              0 bytes
               3 Dir(s)  320,494,665,728 bytes free

 Volume in drive D is DATA
 Volume Serial Number is 6648-288E

 Directory of D:\bkp

09/26/2018  12:38 PM    <DIR>          .
09/26/2018  12:38 PM    <DIR>          ..
09/25/2018  01:47 PM    <DIR>          General_data
               0 File(s)              0 bytes
               3 Dir(s)  320,494,665,728 bytes free

 Volume in drive D is DATA
 Volume Serial Number is 6648-288E

 Directory of D:\bkp

09/26/2018  12:38 PM    <DIR>          .
09/26/2018  12:38 PM    <DIR>          ..
09/25/2018  01:47 PM    <DIR>          General_data
               0 File(s)              0 bytes
               3 Dir(s)  320,494,665,728 bytes free

'''