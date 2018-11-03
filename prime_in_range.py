#!/usr/bin/python
def prime(no1,no2):
	if no2 >= 3:
		num=0
		x=0
		for num in range(no1,no2+1,1):
			if num%2 == 0:
				continue
			for x in range(3, int(num//2) + 2, 1):
				if num%x == 0:
					break
			else:
				print num

def main():
	no1=input("Enter start no")
	no2=input("Enter end no")
	if no1 > no2:
		print "End no should be greater than start no"
	else:
		prime(no1,no2)
	
if __name__ == '__main__':
	main()
	
'''
D:\F DATA\python_class>python prime_in_range.py
Enter start no1
Enter end no100
1
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
'''