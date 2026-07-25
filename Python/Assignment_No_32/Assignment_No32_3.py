import os
import schedule
import time

def DisplayFile(FilePath):
    Ret = os.path.exists(FilePath)

    if(Ret == False):
        print("File is not Present in the current Directory")
        return

    try:
        fobj = open(FilePath,"r")

        Data = fobj.read()

        if(len(Data) == 0):
            print("File",FilePath,"Is Empty")
        else:
            print("Contents Of File Are :")
            print(Data)

        fobj.close()
    except PermissionError as fobj1:
        print("Permission is Denied To Open The File",fobj1)
    except IOError as fobj2:
        print("File Cannot Be Opened",fobj2)

def main():
    FilePath = input("Enter File Path : ")

    print("Automation Script Started")

    schedule.every(1).minute.do(DisplayFile,FilePath)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()
