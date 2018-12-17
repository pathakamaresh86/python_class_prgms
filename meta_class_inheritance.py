#!/usr/bin/python

#decorators do not get applied in inheritance heierarchy, metaclasses get
'''
def debugmethod(cls):
    print("debug method invoked")
    return cls

@debugmethod
class Base(object):
    pass

class Derived(Base):
    pass

b = Base()
d = Derived()
'''

#Using Metaclass
class DebugMethodMeta(type):
    def __init__(self, names, bases, member_dict):
        print("Debug Method Meta Invoked")
        return type.__init__(self, names, bases, member_dict)
#2.7
class BaseMeta:
    __metaclass__ = DebugMethodMeta

class DerivedMeta(BaseMeta):
    pass
b = BaseMeta()
d = DerivedMeta()
	
#for 3.x
'''
class BaseMeta(metaclass = DebugMethodMeta):
    pass
class DerivedMeta(BaseMeta):
    pass        
'''

'''
#With decorator
D:\F DATA\python_class>python meta_class_inheritance.py
Debug Method Meta Invoked

#With metaclasses
D:\F DATA\python_class>python meta_class_inheritance.py
Debug Method Meta Invoked
Debug Method Meta Invoked
'''