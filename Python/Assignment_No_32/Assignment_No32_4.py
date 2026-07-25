import os
import schedule
import time
import shutil

def CopyTextFiles(SourcePath,DestinationPath):
    Ret1 = os.path.exists(SourcePath)
    Ret2 = os.path.exists(DestinationPath)

    if(Ret1 == False):
        print("Marvellous Automation Error : Source Directory Does Not Exist")
        return

    if(Ret2 == False):
        print("Marvellous Automation Error : Destination Directory Does Not Exist")
        return

    fobj = open("CopyLog.txt","a")

    for FolderName , SubFolder , FileName in os.walk(SourcePath):
        for fname in FileName:
            if(fname.endswith(".txt")):
                try:
                    SourceFile = os.path.join(FolderName,fname)
                    DestinationFile = os.path.join(DestinationPath,fname)

                    shutil.copy(SourceFile,DestinationFile)

                    fobj.write("Copied File : "+SourceFile+"\n")
                    print("File",fname,"Gets Copied")
                except Exception as fobj1:
                    fobj.write("Failed To Copy File : "+fname+" -- "+str(fobj1)+"\n")
                    print("Failed To Copy File",fname,fobj1)

    fobj.close()

def main():
    SourcePath = input("Enter Source Directory Path : ")
    DestinationPath = input("Enter Destination Directory Path : ")

    print("Automation Script Started")

    schedule.every(10).minutes.do(CopyTextFiles,SourcePath,DestinationPath)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()
