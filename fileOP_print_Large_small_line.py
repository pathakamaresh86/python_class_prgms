#!/usr/bin/python
#WAP to accept file name and print largest and smallest line in file
import io
def getSmallestAndLargestLine(fname):
	fd=io.FileIO(fname)
	#fd=open(fname)
	smallestLine=""
	largestLine=""
	if fd != None:
		data=fd.readline()
		longlength=len(data)
		shortlength=len(data)
		while True:
			data=fd.readline()
			if data == '':
				break
			if data.startswith("\n"):
				continue
			if longlength < len(data):
				longlength = len(data)
				largestLine = data
			elif shortlength > len(data):
				shortlength = len(data)
				smallestLine = data
	return smallestLine,largestLine		
			
def main():
	fname=input("Enter file name:")
	smallLine,largeLine=getSmallestAndLargestLine(fname)
	print "Small line:", smallLine
	print "Laarge line:", largeLine
	

	
if __name__=="__main__":
	main()
