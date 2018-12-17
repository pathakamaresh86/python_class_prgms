#!/usr/bin/python

def dict_append(x,key,value):
	temp=list()
	if key in x.keys():
		if type(x[key]) == list:
			for val in x[key]:
				temp.append(val)
		else:
			temp.append(x[key])
		temp.append(value)
		x[key]=temp
	else:
		x[key]=value

def dict_delete(x,key,value):
	for key1 in x.keys():
		if key1 == key:
			if type(x[key1]) == list and x[key1].__contains__(value):
				for l1 in x[key1]:
					if l1 == value:
						x[key1].remove(l1)
				if len(x[key1]) == 1:
					for item in x[key1]:
						x[key1]=item
			else:
				if x[key1] == value:
					x.pop(key1)
					
def dict_search(x,key,value):
	for key1 in x.keys():
		if key1 == key:
			if type(x[key1]) == list: 
				if x[key1].__contains__(value):
					print "given key value pair is present in dictionary"
					return
			else:
				if x[key1] == value:
					print "given key value pair is present in dictionary"
					return
	print "Given key value pair is not present in dictionary"
				
					
def dict_display(x):
	for key1 in x.keys():
			if type(x[key1]) == list:
				for l1 in x[key1]:
					print key1,":",l1
			else:
				print key1,":",x[key1]

def menu():
	ch = -1
	while ch < 1 or ch > 6:
		print("Welcome To Dictionary Menu !!!")
		print("1.update\n2.delete\n3.append\n4.search\n5.Display All\n6.Exit")
		ch = input("Enter Choice")
	return ch
	
def dict_operations():
	x=input("Enter dictionary:")
	ch = menu()	
	while(ch != 6):
		if ch == 1:
			key=input("Enter key:")
			value=input("Enter value")
			x[key]=value
			print x
		elif ch == 2:
			key=input("Enter key:")
			value=input("Enter value")
			dict_delete(x,key,value)
			print x
            
		elif ch == 3:
			key=input("Enter key:")
			value=input("Enter value")
			dict_append(x,key,value)
			print x
	
		elif ch == 4:
			key=input("Enter key:")
			value=input("Enter value")
			dict_search(x,key,value)
			print x
		
		elif ch == 5:
			dict_display(x)
		else:
			break
		ch = menu()

def main():
	dict_operations()

if __name__ == "__main__":
	main()

