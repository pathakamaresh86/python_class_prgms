'''
no=0
while(True):
    no=input("no")
    print no
    if no == 0:
        break
else:
    print("else while")
'''

for x in range(1,50):
    print type(x)
    if((x%48)==0):
	    break
    print x
else:
    print("Else-for")
print "hi"

