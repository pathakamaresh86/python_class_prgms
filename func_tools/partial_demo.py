import functools

def add(a, b=2):
    '''simple add function'''
    return a+b

p1 = functools.partial(add, b = 4)
print(p1(10))
print(p1.__doc__)
#print(p1()) #TypeError: add() takes at least 1 argument (1 given)
# Note : Partials work with any callable object, not just standalone function

'''
D:\F DATA\python_class\func_tools>python partial_demo.py
14
partial(func, *args, **keywords) - new function with partial application
    of the given arguments and keywords.

'''

