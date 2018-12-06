#!/usr/bin/python

class SpeedLimitError(Exception):
	def __init__(self,speed):
		self.speed = speed
		
	def __str__(self):
		return "Vehicle Speed is " + str(self.speed) 
		
class SpeedBelowLimit(SpeedLimitError):
	def __init__(self,speed):
		SpeedLimitError.__init__(self,speed)

class SpeedAboveLimit(SpeedLimitError):
	def __init__(self,speed):
		SpeedLimitError.__init__(self,speed)		
	
def main():
	while True:
		speed = input("Enter speed: ")
		try:
			if speed < 20:
				x = SpeedBelowLimit(speed)
				raise x
			elif speed > 80:
				raise SpeedAboveLimit(speed)
			else:
				print "Speed is in limit"
				break
		except SpeedBelowLimit as e:
			print e
		except SpeedAboveLimit as e:
			print e
		
if __name__ == "__main__":
	main()

'''
D:\F DATA\python_class>python exception_handling_class.py
Enter speed: 90
Vehicle Speed is 90
Enter speed: 15
Vehicle Speed is 15
Enter speed: 50
Speed is in limit
'''