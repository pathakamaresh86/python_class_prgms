#!/usr/bin/python  
#shebang line (path for interpreter)
print("Hello World")
x="hello"
print(type(x))
print(x[0])
print(x[-1])
print(x[-4])
print(x[-5])
print(x[1:3])
print(x[::2])
print(x[3::-1]) #x[start_idex:end_index:step_value] stop index is excluded
print(x[:4])
print(x[3:-2]) # no result as positive and negative index point to same
print(x[100:])
print(x[3:1:-1])
print(x[::-1])
y="www.google.com"
print(y[4:-4:])

z=input("Enter no: ") #if entering string enter in double qoutes
print(z)

