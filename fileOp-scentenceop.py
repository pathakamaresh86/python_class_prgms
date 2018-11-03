#!/usr/bin/python

#WAP to accept file name from user and accept a word which should be strating word of scentence. Display all such scentences. 
import io
def printScentences(fname,word):
	fd=io.FileIO(fname)
	scentenceList=[]
	wordList=[]
	if fd != None:
		while True:
			scentenceList=[]
			data=fd.readline()
			if data == '':
				break
			data=data.lower()
			if data.__contains__(word.lower()):
				scentenceList=data.rstrip().lower().split(".")
				#print scentenceList
				for scentence in scentenceList:
					wordList=[]
					wordList=scentence.rstrip().lower().split(" ")
					if wordList[0].lower() == word.lower():
						print scentence
				
				
	fd.close()

def main():
	fname=input("Enter file name:")
	word=input("Enter the starting word to be searched in scnetence:")
	print
	printScentences(fname,word)
	
	
if __name__=="__main__":
	main()

'''

D:\F DATA\python_class>python fileOp-scentenceop.py
Enter file name:"startwordocc.txt"
Enter the starting word to be searched in scnetence:"amaresh"

amaresh vijay pathak
amaresh is good boy
amaresh is sweet boy
amaresh likes food
'''