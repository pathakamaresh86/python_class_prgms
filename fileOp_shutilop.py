#!/usr/bin/python

#Operations on directory and file using shutil and filecmp modules
import shutil as sh
import filecmp as fc

def archiveDir(dir_name):
	return sh.make_archive("myarchive","zip","D:\F DATA\python_class",dir_name)
	

def main():
	'''
	dir_name = input("Enter path of directory name to be archive:")
	archive_name = archiveDir(dir_name)
	print archive_name
	file_name = input("Enter file name to be copied:")
	copy_file="copy-" + file_name
	sh.copy(file_name,copy_file)
	'''
	dir1,dir2 = input("Enter teo directories to be compare:")
	common=["LearningPython.pdf"]
	#tup=fc.cmpfiles(dir1,dir2,common)
	#print tup
	x=fc.dircmp(dir1,dir2)
	print x.report()
	
	
	
	
if __name__ == "__main__":
	main()

