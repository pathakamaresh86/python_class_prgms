#!/usr/bin/python

#WAP to accept file name and print line count word count and char count of the content of file
import io
def calcFileStats(fname):
	fd=io.FileIO(fname)
	#fd=open(fname)
	lineCnt=0
	wordCnt=0
	charCnt=0
	wordList=[]
	if fd != None:
		while True:
			data=fd.readline()
			if data == '':
				break
			data.rstrip()
			lineCnt += 1
			wordList+=data.split(" ")
			charCnt += len(data)
		wordCnt=len(wordList)
	fd.close()
	return lineCnt,wordCnt,charCnt

def main():
	fname=input("Enter file name:")
	lineCnt,wordCnt,charCnt=calcFileStats(fname)
	print "Lines count in file",lineCnt
	print "word count in file",wordCnt
	print "char count in file",charCnt
	
	
if __name__=="__main__":
	main()

'''
D:\F DATA\python_class>python fileOp-filestat.py
Enter file name:"filelines.txt"
Lines count in file 5
word count in file 15
char count in file 108
'''