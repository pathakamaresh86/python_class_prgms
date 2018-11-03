#!/usr/bin/python
#WAP to accept file name and print alternate 10 characters
import io
def readAlternate10char(fname):
	fd=io.FileIO(fname)
	#fd=open(fname)
	cnt=0
	if fd != None:
		while True:
			data=fd.read(10)
			if data == '':
				if cnt == 0:
					fd.seek(10,0)
					data=fd.read(10)
					cnt+=1
				else:
					break
			print data
			fd.seek(10,1)
	fd.close()

def main():
	fname=input("Enter file name:")
	readAlternate10char(fname)

	
if __name__=="__main__":
	main()

'''
D:\F DATA\python_class>python fileOp.py
Enter file name:"a.txt"
amaresh vi
 vvvv xxx
dddddddddd
bbbbbbbb
'''