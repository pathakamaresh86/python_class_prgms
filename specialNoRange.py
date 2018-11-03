#!/usr/bin/python
##WAP to find special numbers in range (sum of digits factorial in number=number) 

def Fact(no):
	if no <= 0 :
		return -1
	elif no == 1:
		return 1
	else:
		return (no * Fact(no-1))
		
def specialNoRange(no1,no2):
	while no1<=no2:
		origno=no1
		sum=0
		while(origno>=1):
			rem = origno%10
			sum = sum + Fact(rem)
			origno = origno//10
		if no1 == sum:
			print no1
		no1 += 1 
	
def main():
	no1,no2 = input("Enter a number range: ")
	if no1 > no2:
		print "End number should be greater than start no"
		return
	specialNoRange(no1,no2)
	
if __name__=="__main__":
	main()