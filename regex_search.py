#!/usr/bin/python
import re

# my logic
'''
def search_occurances(pattern,inp_str):
	length=len(inp_str)
	beg=0
	len_pattern = len(pattern)
	while beg < length:
		search_str=re.search(pattern,inp_str[beg:length])
		print inp_str[beg:length]
		if search_str != None:
			print beg+search_str.start(),beg+search_str.end()
			beg = beg + search_str.end()
		else:
			beg = beg + len_pattern + 1

'''

#sirs logic
'''
def search_occurances(pattern,inp_str):
	result=[]
	match=re.search(pattern,inp_str)
	offset=0
	while match != None:
		result.append((offset+match.start(),offset+match.end()))
		offset += match.end()
		match=re.search(pattern,inp_str[offset:])
	print result
'''

#Using finditer
def search_occurances(pattern,inp_str):
	iter=re.finditer(pattern,inp_str)
	for elem in iter:
		print elem.start(),elem.end()
	
def main():
	pattern=input("Enter pattern to search in string ")
	inp_str=input("Enter string ")
	search_occurances(pattern,inp_str)


if __name__ == "__main__":
	main()
	

'''
D:\F DATA\python_class>python regex_search.py
Enter pattern to search in string 'a'
Enter string "aabcdaaafagaaa"
aabcdaaafagaaa
0 1
abcdaaafagaaa
1 2
bcdaaafagaaa
5 6
aafagaaa
6 7
afagaaa
7 8
fagaaa
9 10
gaaa
11 12
aa
12 13
a
13 14

D:\F DATA\python_class>python regex_search.py
Enter pattern to search in string "ab"
Enter string "ababsdfabaedfabab"
ababsdfabaedfabab
0 2
absdfabaedfabab
2 4
sdfabaedfabab
7 9
aedfabab
13 15
ab
15 17
'''

'''
D:\F DATA\python_class>python regex_search.py
Enter pattern to search in string 'a'
Enter string "aabcdaaafagaaa"
[(0, 1), (1, 2), (5, 6), (6, 7), (7, 8), (9, 10), (11, 12), (12, 13), (13, 14)]

D:\F DATA\python_class>python regex_search.py
Enter pattern to search in string "ab"
Enter string "ababsdfabaedfabab"
[(0, 2), (2, 4), (7, 9), (13, 15), (15, 17)]
'''

'''
D:\F DATA\python_class>python regex_search.py
Enter pattern to search in string "ab"
Enter string "ababsdfabaedfabab"
0 2
2 4
7 9
13 15
15 17
'''