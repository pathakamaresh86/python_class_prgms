#!/usr/bin/python

def main(x):
	i = iter(range(x))
	print (next(i))
	print (next(i))
	print (next(i))
	print (next(i))
	print (next(i))
	#print (next(i))

#boiler-plate
if __name__ == "__main__":
	main(5) 

'''
#if we add next(i) 6 times then at last call it gives stopiteration exception
D:\F DATA\python_class>python iter_ex.py
0
1
2
3
4
Traceback (most recent call last):
  File "iter_ex.py", line 14, in <module>
    main(5)
  File "iter_ex.py", line 10, in main
    print (next(i))
StopIteration

#After commenting 6th call of next(i)
D:\F DATA\python_class>python iter_ex.py
0
1
2
3
4
'''