#!/usr/bin/python
#WAP to accept string from user and print count of vowels in it 
def vowelsCount(str1):
	i=0
	vCnt=0
	l1=['a','e','i','o','u','A','E','I','O','U'] #also u can use string str="aeiouAEIOU"
	while(i< len(str1)):
		x=str1[i]
		if x in l1:
			vCnt = vCnt + 1
		i=i+1
	return vCnt
	
def main():
	str1 = input("Enter string")
	vCnt=vowelsCount(str1)
	print "vowels count ",vCnt
if __name__=="__main__":
	main()