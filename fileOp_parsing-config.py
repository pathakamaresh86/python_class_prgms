#!/usr/bin/python
#WAP to accept file name from user (settings.cfg) and parse that config file 
import io
def parseFile(fname):
	result={}
	outer_result={}
	section_name=""
	fd=io.FileIO(fname)
	section_started=False
	if fd != None:
		#for data in fd:
		while True:
			data=fd.readline()
			if data == '':
				break
			if data.startswith("\n"):
				continue
			if not data.startswith("#"):
				if data.__contains__("="):
					content=data.rstrip().split("=")
					#print content
					if len(content)>1:
						content[1]=content[1].split("#")[0].rstrip()
						result[content[0]]=content[1]
				elif data.__contains__(":"):
					content=data.rstrip().split(":")
					#print content,
					if len(content)>1:
						content[1]=content[1].split("#")[0].rstrip()
						result[content[0]]=content[1]
				else:
					#print content
					content=data.rstrip()
					if section_started:
						outer_result[section_name]=result
						result={}
					section_name=content[1:-1]
					section_started=True
		outer_result[section_name]=result
					
	return outer_result
		
def main():
	configDict={}
	fname=input("Enter file name:")
	configDict=parseFile(fname)
	servername=input("Enter Servername (First/Second/Third):")
	detail=input("Enter Details of server you want to see(ip/monitor/monitor_timeout_in_seconds/top_dump/all:")
	for key in configDict.keys():
		if key.lower() ==  servername.lower():
			if detail.lower() == "all":
				print configDict[key]
			else:
				for item in configDict[key].keys():
					if item.lower().rstrip() == detail.lower():
						print configDict[key][item]
		

	
if __name__=="__main__":
	main()

'''
D:\F DATA\python_class>python fileOp_parsing-config.py
Enter file name:"settings.cfg"
Enter Servername (First/Second/Third):"Second"
Enter Details of server you want to see(ip/monitor/monitor_timeout_in_seconds/top_dump/all:"ip"
 "10.10.10.12"

D:\F DATA\python_class>python fileOp_parsing-config.py
Enter file name:"settings.cfg"
Enter Servername (First/Second/Third):"Third"
Enter Details of server you want to see(ip/monitor/monitor_timeout_in_seconds/top_dump/all:"monitor"
 "no"
'''