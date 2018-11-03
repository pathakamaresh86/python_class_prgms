#!/usr/bin/python
#WAP to accept file name and print alternate 10 bytes print first 10 bytes, skip 11-20 bytes print 21-30 and so on
import io
def readAlternate10Bytes(fname):
	fd=io.FileIO(fname)
	#fd=open(fname)
	if fd != None:
		while True:
			data=fd.read(10)
			if data == '':
				break
			print data
			fd.seek(10,1)
	fd.close()
			
'''
def readAlternate10Bytes(fname):
	fd=io.FileIO(fname)
	if fd != None:
		data=fd.read(10)
		while data !='':
			print data
			fd.seek(10,1)
			data=fd.read(10)
'''

def main():
	fname=input("Enter file name:")
	readAlternate10Bytes(fname)

	
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