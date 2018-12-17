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

if __name__=="__main__":
	consumer=consume()
	#1 way
	next(consumer)
	#2 way
	#consumer.send(None)
	producer = produce(consumer)
	
	for _ in range(20):
		next(producer)

'''
D:\F DATA\python_class>python generator_yield_send_rcv.py
Received : 334
Sent : 334
Received : 663
Sent : 663
Received : 783
Sent : 783
Received : 13
Sent : 13
Received : 727
Sent : 727
Received : 669
Sent : 669
Received : 984
Sent : 984
Received : 460
Sent : 460
Received : 118
Sent : 118
Received : 651
Sent : 651
Received : 229
Sent : 229
Received : 283
Sent : 283
Received : 741
Sent : 741
Received : 994
Sent : 994
Received : 883
Sent : 883
Received : 127
Sent : 127
Received : 321
Sent : 321
Received : 10
Sent : 10
Received : 589
Sent : 589
Received : 410
Sent : 410
'''