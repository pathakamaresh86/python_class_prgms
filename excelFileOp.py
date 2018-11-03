#!/usr/bin/python

#WAP to accept file name from user and accept a word which sheetould be strating word of scentence. Display all such scentences. 


# Reading an excel file using Python 
import xlrd 
def parseExcelFile(fname):
	# To open Workbook 
	fname=fname.rstrip()
	wb = xlrd.open_workbook(fname)
	sheet = wb.sheet_by_index(0)
	for i in range(sheet.ncols): 
		print(sheet.cell_value(0, i))
	for i in range(sheet.nrows):
		print(sheet.row_values(i))
	s = ""
	ph = "BEGIN:VCARD\nVERSION:2.1\nN:;"
	for i in range(1,sheet.nrows):
		if(sheet.cell_value(i,sheet.ncols-1)):
			s+=ph+str(sheet.cell_value(i,0))+";;;\nFN:"+str(sheet.cell_value(i,0))+"\nTEL;CELL;PREF:"+str(sheet.cell_value(i,2))+"\nTEL;HOME:"+str(sheet.cell_value(i,3))+"\nADR;HOME:"+str(sheet.cell_value(i,1))+"\nEMAIL:"+str(sheet.cell_value(i,4))+"\nEND:VCARD\n"
	text_file = open("testvcf.vcf", "w")
	text_file.write(s)
	text_file.close()
	print "Completed!"

def main():
	fname=input("Enter excel file to parse: ")
	parseExcelFile(fname)
	
	
if __name__=="__main__":
	main()

'''
D:\F DATA\python_class>python excelFileOp.py
Enter excel file to parse: "test.xlsx"
Name
Address
Mobile
Home Number
Email Id
[u'Name', u'Address', u'Mobile', u'Home Number', u'Email Id']
[u'Amaresh', u'Pune', 123.0, 234.0, u'amaresh@a.b']
[u'Mayura', u'Pune', 456.0, 890.0, u'mayu@w.e']
[u'asd', u'e', 54.0, 34.0, u'asd@w.e']
Completed!

testvcf.vcf
BEGIN:VCARD
VERSION:2.1
N:;Amaresh;;;
FN:Amaresh
TEL;CELL;PREF:123.0
TEL;HOME:234.0
ADR;HOME:Pune
EMAIL:amaresh@a.b
END:VCARD
BEGIN:VCARD
VERSION:2.1
N:;Mayura;;;
FN:Mayura
TEL;CELL;PREF:456.0
TEL;HOME:890.0
ADR;HOME:Pune
EMAIL:mayu@w.e
END:VCARD
BEGIN:VCARD
VERSION:2.1
N:;asd;;;
FN:asd
TEL;CELL;PREF:54.0
TEL;HOME:34.0
ADR;HOME:e
EMAIL:asd@w.e
END:VCARD

'''