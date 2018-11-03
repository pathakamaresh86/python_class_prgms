#!/usr/bin/python

def withFactRec(no):
	if no <= 0 :
		return -1
	elif no == 1:
		return 1
	else:
		return (no * withFactRec(no-1))
		
def withoutFactRec(no):
	if no <= 0 :
		return -1
	elif no == 1:
		return 1
	else:
		fact = 1
		for x in range(2,no+1):
			fact = fact * x
		return fact
		
def main():
	no = input("Enter a number for finding facorital : ")
	result01 = withFactRec(no)
	if(result01 == -1):
		print ("Invalid Number")
	else:
		print ("With Recurtion : ", result01)

	result02 = withoutFactRec(no)
	if(result02 == -1):
		print ("Invalid Number")
	else:
		print ("With-out Recurtion : ", result02)
	
if __name__=="__main__":
	main()

'''
D:\F DATA\python_class>python factorial.py
Enter a number for finding facorital : 6
('With Recurtion : ', 720)
('With-out Recurtion : ', 720)
'''