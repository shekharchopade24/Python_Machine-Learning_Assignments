import os
import schedule
import time
import datetime

def DirectoryScanner(DirectoryPath):
    TotalFiles = 0
    TotalSubDir = 0

    for FolderName , SubFolder , FileName in os.walk(DirectoryPath):
        TotalFiles = TotalFiles + len(FileName)
        TotalSubDir = TotalSubDir + len(SubFolder)

    timeStamp = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    print("Directory Scanned:",DirectoryPath)
    print("Total Files:",TotalFiles)
    print("Total Subdirectories:",TotalSubDir)
    print("Scan Time:",timeStamp)

def main():
    DirectoryPath = input("Enter Directory Name : ")

    print("Automation Script Started")

    schedule.every(1).minute.do(DirectoryScanner,DirectoryPath)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()
