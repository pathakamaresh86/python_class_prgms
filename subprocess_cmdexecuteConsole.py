#!/usr/bin/python
#WAP to copy o/p of given list of commands on console preceded by command name and execution time.
import subprocess
import datetime

def fun1(cmd):
	print cmd
	print datetime.datetime.now()

def execListofCmds(cmds):
	for cmd in cmds:
		x=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE, preexec_fn=fun1(cmd), shell=True)
		tup= x.communicate()
		if tup[1] == None:
			print tup[0]
		else:
			print tup[1]

def main():
		cmds=[]
		cmds=input("Enter list of commands to be executed")
		execListofCmds(cmds)

if __name__ == "__main__":
		main()
