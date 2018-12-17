#!/usr/bin/python

import random

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

def WrapperConsume(func):
	def init():
		consumer = func()
		next(consumer)
		return consumer
	return init
	
if __name__=="__main__":
	init_consumer = WrapperConsume(consume)
	consumer = init_consumer()
	producer = produce(consumer)
	
	for _ in range(20):
		next(producer)


'''
D:\F DATA\python_class>python generator_initializing_consumer_Wrapper.py
Received : 728
Sent : 728
Received : 87
Sent : 87
Received : 833
Sent : 833
Received : 224
Sent : 224
Received : 773
Sent : 773
Received : 795
Sent : 795
Received : 776
Sent : 776
Received : 254
Sent : 254
Received : 693
Sent : 693
Received : 367
Sent : 367
Received : 768
Sent : 768
Received : 985
Sent : 985
Received : 834
Sent : 834
Received : 724
Sent : 724
Received : 550
Sent : 550
Received : 247
Sent : 247
Received : 431
Sent : 431
Received : 49
Sent : 49
Received : 458
Sent : 458
Received : 692
Sent : 692
'''