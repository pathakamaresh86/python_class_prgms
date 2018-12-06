import threading
import time
def worker(num):
	"""thread worker function"""
	time.sleep(1)
	print threading.currentThread().getName()
	print 'Worker: %s' % num

threads = []
for i in range(5):
	t = threading.Thread(target=worker, args=(i,), name="t"+str(i)) #args need tuple so we mention args=(i,)
	threads.append(t)
	print("Thread %d Started\n"%i)
#	t.start()
#	t.join()

for y,x in enumerate(threads):
	if(y==2):
		x.setDaemon(True);
print("All Threads Started\n")
for x in threads:
	x.start()
for x in threads:
	print x.isAlive(), x.isDaemon()
for x in threads:
	x.join()
print("Main Done\n")

'''
D:\F DATA\python_class>python thread_func_arg.py
Thread 0 Started

Thread 1 Started

Thread 2 Started

Thread 3 Started

Thread 4 Started

All Threads Started

True False
True False
True True
True False
True False
t0t1t2
Worker: 2


Worker: 1Worker: 0t4t3
Worker: 3



Worker: 4
Main Done
'''