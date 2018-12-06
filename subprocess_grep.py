#!/usr/bin/python
#WAP to accept filename from user and run grep cmd for specified content in file w/o explicitely reading it.
import subprocess

def execGrep(file_name,content):
	x=subprocess.Popen(["cat",file_name],stdout=subprocess.PIPE)
	y=subprocess.Popen(["grep","-i",content],stdin=x.stdout,stdout=subprocess.PIPE)
	print y.communicate()

def main():
	file_name=input("Enter file name ")
	content=input("Enter string to be searched in file name ")
	execGrep(file_name,content)

if __name__ == "__main__":
		main()

'''
bash-4.1$ python subprocess_grep.py
Enter file name "ama.txt"
Enter string to be searched in file name "amaresh"
('amaresh vijay pathak\nAmaresh\n', None)
'''