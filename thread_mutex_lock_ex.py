from threading import Thread
from threading import Lock           
import time

threads = []
data = 0
lock = Lock()

def get_job():
	global data #if we want to access global variable inside local function use global keyword  
	lock.acquire()
	data += 1
	time.sleep(0.1)
	x= data #here we assign data to x and return x as if within releaseing lock and returning data if new thread gets schedule then data might get modified so using local variable
	lock.release()
	return x
	

def process_job():
	print get_job()
	#global data
	#print data

for i in range(10):
	thread = Thread(target=process_job)
	threads.append(thread)
	thread.start()

for thread in threads:
	thread.join()

'''
D:\F DATA\python_class>python thread_mutex_lock_ex.py
1
2
3
4
5
6
7
8
9
10
'''