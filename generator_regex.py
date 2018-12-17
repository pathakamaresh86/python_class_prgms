#!/usr/bin/python
import re

def GeneratorGrep(pattern, file_name):
	'''
	Search for a regex pattern in a file
	'''
	fd=open(file_name)
	pat = re.compile(pattern)
	for line in fd:
		if pat.search(line):
			yield line
	fd.close()

def main():
	file_name = input("Enter File Name from which to extract single line comments:")
	comment_line_generator = GeneratorGrep("\A#", file_name)
	#for line in comment_line_generator:
	#	print(line)
	
	print next(comment_line_generator)
	print next(comment_line_generator)
	print next(comment_line_generator)
	
if __name__ == "__main__":
	main()

'''
D:\F DATA\python_class>python generator_regex.py
Enter File Name from which to extract single line comments:"audio.conf"
# Configuration file for the audio service

# This section contains options which are not specific to any

# particular interface

# Switch to master role for incoming connections (defaults to true)

# If we want to disable support for specific services

# Defaults to supporting all implemented services

#Disable=Gateway,Source,Socket
'''

'''
instead of for you just print the next of generatot
D:\F DATA\python_class>python generator_regex.py
Enter File Name from which to extract single line comments:"audio.conf"
# Configuration file for the audio service

# This section contains options which are not specific to any

# particular interface

'''