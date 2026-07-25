import os
import schedule
import time
import datetime

def CountFiles(DirectoryPath):
    Ret = os.path.exists(DirectoryPath)

    if(Ret == False):
        print("Marvellous Automation Error : There is no such directory with Name",DirectoryPath)
        return

    TotalFiles = 0

    for FolderName , SubFolder , FileName in os.walk(DirectoryPath):
        TotalFiles = TotalFiles + len(FileName)

    timeStamp = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    fobj = open("DirectoryCountLog.txt","a")
    fobj.write("Directory Path: "+DirectoryPath+"\n")
    fobj.write("Number of Files: "+str(TotalFiles)+"\n")
    fobj.write("Date and Time: "+timeStamp+"\n\n")
    fobj.close()

    print("Directory Path :",DirectoryPath,"Number of Files :",TotalFiles)

def main():
    DirectoryPath = input("Enter Directory Name : ")

    print("Automation Script Started")

    schedule.every(5).minutes.do(CountFiles,DirectoryPath)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()
