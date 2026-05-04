#!/usr/bin/python
#Little function that checks if a loFile exists, if not it creates the file
import logging, os, time

logFile = "/path/to/logfiles/dataLogFile.log"

def checkForFile():
#Check if a log file exists, if not create one.
    if os.path.exists(logFile):
        myFileDocs  = open(logFile, 'a')
    else:
        myFileDocs = open(logFile, 'wb')

def main():
    #Stuff starts happening here.
    pass

if __name__ == "__main__":
    checkForFile()
    #Start logging
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s', filename=logFile)
    logging.info("Running script")
    main()
