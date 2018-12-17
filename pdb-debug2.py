#!/usr/bin/python
import pdb
import traceback

def Factorial(n):
    if n == 0 or n == 1:
        return 1
    if n == 2:
        #pdb.set_trace()
        return 2
    traceback.print_stack()
    return n*Factorial(n-1)

def main():
    number = input("Enter Number:")
    print(Factorial(number))

if __name__ == "__main__":
    main()

'''
D:\F DATA\python_class>python pdb-debug2.py
Enter Number:5
  File "pdb-debug2.py", line 19, in <module>
    main()
  File "pdb-debug2.py", line 16, in main
    print(Factorial(number))
  File "pdb-debug2.py", line 11, in Factorial
    traceback.print_stack()
  File "pdb-debug2.py", line 19, in <module>
    main()
  File "pdb-debug2.py", line 16, in main
    print(Factorial(number))
  File "pdb-debug2.py", line 12, in Factorial
    return n*Factorial(n-1)
  File "pdb-debug2.py", line 11, in Factorial
    traceback.print_stack()
  File "pdb-debug2.py", line 19, in <module>
    main()
  File "pdb-debug2.py", line 16, in main
    print(Factorial(number))
  File "pdb-debug2.py", line 12, in Factorial
    return n*Factorial(n-1)
  File "pdb-debug2.py", line 12, in Factorial
    return n*Factorial(n-1)
  File "pdb-debug2.py", line 11, in Factorial
    traceback.print_stack()
120
'''