#!/usr/bin/python
def vowelsCount(str1):
	l1=["a","e","i","o","u","A","E","I","O","U"]
	#print [x for x in str1 if x in l1]
	print [x for x in str1 if x in "aeiouAEIOU"]

def main():
	str1 = input("Enter string")
	vowelsCount(str1)

if __name__ == "__main__":
	main()
	
'''
D:\F DATA\python_class>python list_comprehension_vowels.py
Enter string"amareshAdfgIOkjioUu"
['a', 'a', 'e', 'A', 'I', 'O', 'i', 'o', 'U', 'u']
'''