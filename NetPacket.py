#!/usr/bin/python

def Packetize(crc, flag, len, data):
	packet = crc & 127
	packet = packet << 1
	packet = packet | (flag & 1)
	packet = packet << 9
	packet = packet | (len & 511)
	packet = packet << 15
	packet = packet | (data & ((1<<15)-1))
	return packet

def Depacketize(packet):
	data = packet & ((1<<15)-1)
	packet = packet >> 15
	len = packet & ((1<<9)-1)
	packet = packet >> 9
	flag = packet & 1
	packet = packet >> 1
	crc = packet & ((1<<7)-1)
	return crc, flag, len, data

def main():
	crc = input("Enter crc less than 127: ")
	flag = input("Enter flag 0 or 1: ")
	len = input("Enter len less than 511: ")
	data = input("Enter data less than 32767: ")
	packet = Packetize(crc, flag, len, data)
	print "Network Packet", packet
	crc,flag,len,data = Depacketize(packet)
	print "Depacketize data", crc, flag, len, data
	
	
if __name__=="__main__":
	main()
	
'''
D:\F DATA\python_class>python NetPacket.py
Enter crc: 29
Enter flag: 1
Enter len: 81
Enter data: 1023
Network Packet 992510975
Depacketize data 29 1 81 1023
'''