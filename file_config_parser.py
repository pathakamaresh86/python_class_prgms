#!/usr/bin/python

#Parse Config file using configparser module
import ConfigParser as CFP

def parseConfigFile(cfg_file_name):
    parser = CFP.ConfigParser()
    parser.read(cfg_file_name)
    print parser.sections()
    print parser.options("Second")
    print parser.get("Second", "ip")
    print parser.items("First","")

def main():
    cfg_file_name = input("Enter Configuration File Name:")
    parsed_configurations = parseConfigFile(cfg_file_name)

if __name__ == "__main__":
    main()

'''
D:\F DATA\python_class>python file_config_parser.py
Enter Configuration File Name:"settings.cfg"
['First', 'Second', 'Third']
['ip', 'monitor', 'monitor_timeout_in_seconds', 'top_dump']
"10.10.10.12" #This is the Comment
'''