#!/usr/bin/python

#WAP to accept 3 files 1st file names, 2nd address, 3rd file mobile number create output file as amaresh,pune,98;pranjali,mumbai,88. 
import io
def writeRecordsTofile(name_file,address_file,phoneNo_file,record_file):
	fd_name=io.FileIO(name_file)
	fd_addr=io.FileIO(address_file)
	fd_mob=io.FileIO(phoneNo_file)
	str_rec=""
	if fd_name != None and fd_addr != None and fd_mob != None:
		while True:
			name=fd_name.readline()
			addr=fd_addr.readline()
			mobile=fd_mob.readline()
			if name == '' or addr == '' or mobile == '':
				break
			str_rec += name.rstrip() + ", " + addr.rstrip() + ", " + mobile.rstrip() + "; "
		str_rec.rstrip(";")
		fd_record=io.FileIO(record_file,"w")
		fd_record.write(str_rec)
		fd_record.close()
	fd_name.close()
	fd_addr.close()
	fd_mob.close()

def main():
	name_file=input("Enter file name having Person names:")
	address_file=input("Enter file name having address:")
	phoneNo_file=input("Enter file name having phone numbers:")
	record_file=input("Enter file name where records will be stored:")
	writeRecordsTofile(name_file,address_file,phoneNo_file,record_file)
	
	
if __name__=="__main__":
	main()

'''

D:\F DATA\python_class>python fileOp-fileReadWriteRecord.py
Enter file name having Person names:"name.txt"
Enter file name having address:"addr.txt"
Enter file name having phone numbers:"phone.txt"
Enter file name where records will be stored:"record-details.txt"

record-details.txt
amaresh pathak, Sinhagad road pune, 9850728760; vijay pathak, Tilak road pune, 9922921361; Vidya Pathak, Sadashiv Peth Pune, 9850783550; Mayura Pathak, SB Road Pune, 9850678707; Pranjali Pathak, Kothrud Pune, 9673470988; 

'''