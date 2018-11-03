#!/usr/bin/python
#WAP to accept string from user and print count of vowels in it 
def amstrongRange(no1,no2):
	while no1<=no2:
		origno=no1
		sumofcubes=0
		while(origno>=1):
			rem = origno%10
			sumofcubes = sumofcubes + rem**3
			origno = origno//10
		if no1 == sumofcubes:
			print no1
		no1 += 1 
	
def main():
	no1,no2 = input("Enter a number range: ")
	if no1 > no2:
		print "End number should be greater than start no"
		return
	amstrongRange(no1,no2)
	
if __name__=="__main__":
	main()