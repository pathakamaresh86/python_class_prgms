#!/usr/bin/python
#WAP to accept file name from user (audio.conf) and parse that file
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
				#if data.__contains__("="):
				content=data.rstrip().split("=")
				#print content
				if len(content)>1:
					content[1]=content[1].split("#")[0].rstrip()
					result[content[0]]=content[1]
				else:
					#print content
					if section_started:
						outer_result[section_name]=result
						result={}
					section_name=content[0][1:-1]
					section_started=True
				#elif data.__contains__(":"):
				#	content=data.rstrip().split(":")
				#	print content,
				#	result[content[0]]=content[1]
				#else:
				#	print data,
		outer_result[section_name]=result
					
	print
	print outer_result
'''
for 3.x,
while True:
	line=fd.readline()
	if line=b'':
		break;
	line=str(line) #this is req as 3.x consider by default line as bytes 
	data.startswith('b\'#')
'''		
def main():
	fname=input("Enter file name:")
	parseFile(fname)

	
if __name__=="__main__":
	main()
	

'''
D:\F DATA\python_class>python fileOp_parsing.py
Enter file name:"conf.txt"
abc=3
pqr=5
asd:1
fr:2

D:\F DATA\python_class>python fileOp_parsing.py
Enter file name:"conf.txt"
['abc', '3\r\n'] ['pqr', '5\r\n'] ['asd', '1\r\n'] ['fr', '2\r\n']


final
D:\F DATA\python_class>python fileOp_parsing.py
Enter file name:"conf.txt"
['abc', '3'] ['pqr', '5'] ['asd', '1'] ['fr', '2']

D:\F DATA\python_class>python fileOp_parsing.py
Enter file name:"audio.conf"

{'Headset': {'HFP': 'true', 'MaxConnected': '1', 'FastConnectable': 'false'}, 'A2DP': {'MPEG12Sources': '0', 'SBCSources': '1'}, 'General': {'AutoConnect': 'true', 'SCORouting': 'PCM', 'Master': 'true'}}
'''