#!/usr/bin/python
class Person:

	def __init__(self, name, addr, mob, adhar_no, gender):
		self.name = name
		self.addr = addr
		self.mob = mob
		self.adhar_no = adhar_no
		self.gender = gender
		
	def getPersonName(self):
		return self.name
	
	def setPersonName(self,pName):
		self.name=pName
		
	def getAddress(self):
		return self.addr
	
	def setAddress(self,paddr):
		self.addr=paddr
