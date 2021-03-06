#!/usr/bin/python
#WAP to copy o/p of given list of commands in file preceded by command name and execution time.
import subprocess
import datetime

def fun1(cmd):
        fd=open("cmdExecOp.txt", "a")
        fd.write("\n")
        fd.write(cmd)
        fd.write("\n")
        fd.write(str(datetime.datetime.now()))
        fd.write("\n")
        fd.close()

def execListofCmds(cmds):
        for cmd in cmds:
                fd=open("cmdExecOp.txt", "a")
                x=subprocess.Popen([cmd],stdout=fd,stderr=fd, preexec_fn=fun1(cmd),shell=True)
                x.communicate()
                fd.close()

def main():
        cmds=[]
        cmds=input("Enter list of commands to be executed")
        #fd=open("cmdExecOp.txt", "a")
        execListofCmds(cmds)
        #fd.close()

if __name__ == "__main__":
        main()

'''
bash-4.1$ cat cmdExecOp.txt

date
2018-11-27 15:04:28.767882
Tue Nov 27 15:04:28 IST 2018

pwd
2018-11-27 15:04:28.772332
/oracle

ls -ltr
2018-11-27 15:04:28.775463
total 10016
lrwxrwxrwx 1 oracle     1002      20 May  2  2016 12.1.0 -> /data1/oracle/12.1.0
lrwxrwxrwx 1 oracle     1002      19 May  2  2016 grid -> /data1/oracle/grid/
-rwxrwxrwx 1 oracle     1002      62 May 17  2016 neelu.setup
drwxrwxrwx 2 oracle     1002    4096 Sep  8  2016 Ragini_tc
lrwxrwxrwx 1 oracle     1002      20 Sep 28  2016 11.2.0 -> /data1/oracle/11.2.0
drwxrwxrwx 5 oracle     1002    4096 Sep 28  2016 oraInventory
drwxrwxrwx 3 oracle     1002    4096 Sep 28  2016 oradiag_oracle
drwxr-xr-x 3 oracle     1002    4096 Oct 13  2017 +OBTDG1
-rwxrwx--- 1 oracle     1002    1604 Oct 17  2017 dupdb.sh
-rw-r--r-- 1 oracle     1002       0 Jan  3  2018 0
-rw-r--r-- 1 oracle     1002     326 Feb  8  2018 recover_script_dtorestore_1774.1518070151
-rwxrwx--- 1 oracle     1002    5709 Feb  8  2018 recover_script
-rw-r--r-- 1 oracle     1002 2474357 Mar  7  2018 -verbose
drwxr-xr-x 2 oracle     1002    4096 Mar 21  2018 FAV
drwxr-xr-x 2 oracle     1002    4096 Mar 30  2018 DUP
drwxrwxr-x 3 oracle     1002    4096 Apr  5  2018 04
-rwxrwx--- 1 oracle     1002    3863 Apr 19  2018 y
-r--r--r-- 1 oracle     1002    7624 May  2  2018 obt.profile
-rw-r--r-- 1 oracle oracle       773 May 17  2018 pfile.ora
drwxrwxr-x 2 oracle oinstall    4096 Jun 12 18:39 1
drwxrwxr-x 2 oracle oinstall    4096 Jun 12 18:39 3
drwxrwxr-x 2 oracle oinstall    4096 Jun 12 18:44 Y
drwxr-xr-x 8 oracle oinstall    4096 Aug 10 13:49 Root
-rw-r--r-- 1 oracle oinstall 7601173 Aug 10 13:54 Root.zip
-rw------- 1 oracle oinstall   71173 Sep 12 05:45 nohup.out
drwxrwxr-x 2 oracle oinstall    4096 Oct 26 07:45 use_db_recovery_file_dest
-rw-rw-r-- 1 oracle oinstall     321 Oct 26 09:26 enable_flashback.out
drwxr-xr-x 2 oracle oinstall    4096 Nov 23 17:33 tmp2
-rw-r--r-- 1 oracle oinstall     735 Nov 27 15:04 abc.py
-rw-r--r-- 1 oracle oinstall     138 Nov 27 15:04 cmdExecOp.txt

echo hi
2018-11-27 15:04:28.781735
hi

cp
2018-11-27 15:04:28.784188
cp: missing file operand
Try `cp --help' for more information.
'''
