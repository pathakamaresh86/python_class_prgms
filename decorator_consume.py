#!/usr/bin/python

import random

def WrapperConsume(func):
	print "Invokes Wrapper at loading"
	#name of init cna be different
	def init():
		consumer = func()
		next(consumer)
		return consumer
	return init

@WrapperConsume
def consume():
	while True:
		data = yield #data came from send method
		print("Received : {}".format(data))
		
def produce(consumer):
	while True:
		data= random.randint(1,1000)
		consumer.send(data)
		print("Sent : {}".format(data))
		yield #to stop going into infinite loop

	
if __name__=="__main__":
	#By explicitely calling wrapper function
	#init_consumer = WrapperConsume(consume)
	#consumer = init_consumer()
	
	#By using decorator
	consumer = consume() # consume calls inner function init 
	producer = produce(consumer)
	
	for _ in range(20):
		next(producer)


'''
D:\F DATA\python_class>python
Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import decorator_consume
Invokes Wrapper at loading

D:\F DATA\python_class>python decorator_consume.py
Invokes Wrapper at loading
Received : 629
Sent : 629
Received : 483
Sent : 483
Received : 292
Sent : 292
Received : 626
Sent : 626
Received : 184
Sent : 184
Received : 919
Sent : 919
Received : 175
Sent : 175
Received : 468
Sent : 468
Received : 524
Sent : 524
Received : 312
Sent : 312
Received : 299
Sent : 299
Received : 750
Sent : 750
Received : 757
Sent : 757
Received : 630
Sent : 630
Received : 490
Sent : 490
Received : 205
Sent : 205
Received : 98
Sent : 98
Received : 154
Sent : 154
Received : 966
Sent : 966
Received : 417
Sent : 417
'''