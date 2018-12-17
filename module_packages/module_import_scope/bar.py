#!/usr/bin/python
from foo import foo
a = 100
def test():
    print("test of bar")

def bar():
    global a
    print(a)
    foo()
    print(a)
    test()

if __name__ == "__main__":
    bar()
    
'''
D:\F DATA\python_class\module_packages\module_import_scope>python bar.py
100
10
20
test of foo
100
test of bar
'''