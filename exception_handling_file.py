#!/usr/bin/python

def main():
	try:
		fd=open("vijay.txt")
		try:
			fd.write("Hello")
		#except:
		finally:
			print "file open in read mode so cant write to it"
			fd.close()
	except Exception as e:
		#print "exception",e
		print("exception", e)
	finally:
		print "Execute always!!!"

if __name__ == "__main__":
	main()

'''
#with except:
D:\F DATA\python_class>python exception_handling_file.py
file oen in read mode so cant write to it
Execute always!!!

#with finally:
D:\F DATA\python_class>python exception_handling_file.py
file open in read mode so cant write to it
exception File not open for writing
Execute always!!!
'''