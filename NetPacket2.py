#!/usr/bin/python

def Packetize(flag, crc, reserved, len, data):
	packet = flag & 3 # packet|(flag&(1<<2-1))
	packet = packet << 5
	packet = packet | (crc & 31) #31=((1<<5)-1)
	packet = packet << 3
	packet = packet | (reserved & 7)
	packet = packet << 9
	packet = packet | (len & 511)
	packet = packet << 13
	packet = packet | (data & ((1<<13)-1))
	return packet

def Depacketize(packet):
	data = packet & ((1<<13)-1)
	packet = packet >> 13
	len = packet & ((1<<9)-1)
	packet = packet >> 9
	reserved = packet & ((1<<3)-1)
	packet = packet >> 3
	crc = packet & ((1<<5)-1)
	packet = packet >> 5
	flag = packet & ((1<<2)-1)
	return flag, crc, reserved, len, data

def main():
	flag = input("Enter flag less than 2: ")
	crc = input("Enter crc less than 31:")
	reserved = input("Enter reserved less than 8: ")
	len = input("Enter len less than 511: ")
	data = input("Enter data less than 8191: ")
	packet = Packetize(flag, crc, reserved, len, data)
	print "Network Packet", packet
	flag,crc,reserved,len,data = Depacketize(packet)
	print "Depacketize data", flag, crc, reserved, len, data
	
	
if __name__=="__main__":
	main()
	
'''
D:\F DATA\python_class>python NetPacket2.py
Enter flag less than 2: 1
Enter crc less than 31:29
Enter reserved less than 8: 5
Enter len less than 511: 81
Enter data less than 8191: 2000
Network Packet 2068457424
Depacketize data 1 29 5 81 2000
'''