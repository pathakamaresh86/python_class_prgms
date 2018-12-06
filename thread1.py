import threading
import time
def worker():
	while True:
		"""thread worker function"""
		print "worker"
		print "1"
		time.sleep(1)

if __name__ == '__main__':
	t = threading.Thread(target=worker) #here we pass function address to thread and not invoking the function
	t.setDaemon(True) # making thread as deamon thread so it wont finish/kill
	t.start()
	t.join()
'''
threads = []
for i in range(5):
	t = threading.Thread(target=worker)
	threads.append(t)
	t.start()'''
	
'''
if we not add t.join() then after printing worker it stops as main thread finishes
w/o t.join()
o/p 
worker

with t.join:
worker
1
worker
1
...
.,,,
