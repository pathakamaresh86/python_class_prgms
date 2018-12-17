import logging

#logging.basicConfig(filename='log_to_file.out', level=logging.ERROR) #print only error and critical logs to file
logging.basicConfig(filename='log_to_file.out', level=logging.DEBUG)  #print debug,error,critical log in file
logging.debug('This message should go to the log file')
logging.error('This message should go to the log file')
logging.critical('This message should go to the log file')
