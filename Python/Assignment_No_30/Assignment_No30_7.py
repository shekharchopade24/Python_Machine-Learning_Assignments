import schedule
import time
import datetime
import shutil
import os

def BackupFile(SourcePath,DestinationPath):
    timeStamp = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

    BaseName = os.path.basename(SourcePath)
    Name,Ext = os.path.splitext(BaseName)

    NewName = Name+"_"+timeStamp+Ext

    DestinationFile = os.path.join(DestinationPath,NewName)

    shutil.copy(SourcePath,DestinationFile)

    LogTime = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    fobj = open("backup_log.txt","a")
    fobj.write("Backup completed successfully at "+LogTime+"\n")
    fobj.close()

    print("Backup completed successfully at",LogTime)

def main():
    SourcePath = input("Enter Source File Path : ")
    DestinationPath = input("Enter Destination Directory Path : ")

    print("Automation Script Started")

    schedule.every(1).hour.do(BackupFile,SourcePath,DestinationPath)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()
