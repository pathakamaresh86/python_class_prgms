#!/usr/bin/python

#WAP to accept file name, word and its occurance count from user print lines from file which hava that word occuring specified number of times 
import io
def printFileLines(fname,word,wCnt):
	fd=io.FileIO(fname)
	wordList=[]
	if fd != None:
		while True:
			wordList=[]
			data=fd.readline()
			if data == '':
				break
			wordList=data.rstrip().lower().split(" ")
			if wordList.count(word.lower()) == wCnt:
				print data,
	fd.close()

def main():
	fname=input("Enter file name:")
	word=input("Enter the word to be searched:")
	wCnt=input("Enter the count of word:")
	print
	printFileLines(fname,word,wCnt)
	
	
if __name__=="__main__":
	main()

'''

D:\F DATA\python_class>python fileOp-WordOcuurance.py
Enter file name:"file-wordocc.txt"
Enter the word to be searched:"vijay"
Enter the count of word:2

Mayura vijay pathak vijay
Vijay vijay Devidas pathak
'''