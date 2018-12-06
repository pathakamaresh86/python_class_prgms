from threading import Thread, Event
import time
data = []
produce_event = Event()
consume_event = Event()

def read():
	global data
	while True:
		if len(data) == 0:
			produce_event.clear()
			produce_event.wait()
		print "\nConsumed ", data[0]
		if data[0] == "end":
			consume_event.set()
			break
		del data[0]
		consume_event.set()
		time.sleep(1)

def write():
	global data
	while True:
		if len(data) == 10:
			consume_event.clear()
			consume_event.wait()
		val = input("Enter Data (to stop enter end):-")
		data.append(val)
		if val == "end":
			produce_event.set()
			break
			
		if len(data) == 10:
			produce_event.set()
		time.sleep(0.1)

consumer = Thread(target=read, name="consumer")
producer = Thread(target=write, name= "producer")
consumer.start()
producer.start()

consumer.join()  # Wait for the threads to finish naturally
producer.join()
print "done"

'''
D:\F DATA\python_class>python thread-producer-consumer.py
Enter Data (to stop enter end):-"A"
Enter Data (to stop enter end):-"b"
Enter Data (to stop enter end):-"c"
Enter Data (to stop enter end):-"d"
Enter Data (to stop enter end):-"e"
Enter Data (to stop enter end):-"f"
Enter Data (to stop enter end):-"g"
Enter Data (to stop enter end):-"h"
Enter Data (to stop enter end):-"i"
Enter Data (to stop enter end):-"j"

Consumed  A
Enter Data (to stop enter end):-
Consumed  b

Consumed  c

Consumed  d

Consumed  e

Consumed  f

Consumed  g

Consumed  h

Consumed  i

Consumed  j
"k"
Enter Data (to stop enter end):-"l"
Enter Data (to stop enter end):-"end"

Consumed  k

Consumed  l

Consumed  end
done
'''