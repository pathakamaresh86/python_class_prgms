#!/usr/bin/python

# Program using map and filter
fd = open("lambda_line_test.txt")
lines = fd.readlines()

ch_count=map(lambda x : len(x), lines)
word_count=map(lambda x : len(x.split(" ")), lines)
filter_data=filter(lambda x : x > 10, [1,11,3,12,4,20,30,9])
reduce_data=reduce(lambda x,y : x + y, [1,2,3,4,5,6,7,8,9,10])
reduce_data1=reduce(lambda x,y : x + y, range(1,11))

print ch_count
print word_count
print filter_data
print reduce_data
print reduce_data1

#for 3.x map returns map object so to print data we need to traverse in loop
#for i in ch_count:
#	print i

fd.close()

'''
D:\F DATA\python_class>python lambda_to_print_line_length.py
[15, 8, 6, 9]
[2, 1, 1, 1]
[11, 12, 20, 30]
55
55
'''