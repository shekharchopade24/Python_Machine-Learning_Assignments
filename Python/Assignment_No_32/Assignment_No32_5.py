import os
import schedule
import time

def DeleteEmptyFiles(DirectoryPath):
    fobj = open("EmptyFileDeleteLog.txt","a")

    for FolderName , SubFolder , FileName in os.walk(DirectoryPath):
        for fname in FileName:
            try:
                FilePath = os.path.join(FolderName,fname)

                if(os.path.getsize(FilePath) == 0):
                    os.remove(FilePath)
                    fobj.write("Deleted File : "+FilePath+"\n")
                    print("Deleted Empty File :",FilePath)
            except PermissionError as fobj1:
                fobj.write("Permission Denied For File : "+fname+"\n")
                print("Permission Denied For File",fname,fobj1)

    fobj.close()

def main():
    DirectoryPath = input("Enter Directory Name : ")

    print("Automation Script Started")

    schedule.every(1).hour.do(DeleteEmptyFiles,DirectoryPath)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()
