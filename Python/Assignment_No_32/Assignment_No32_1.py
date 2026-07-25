import schedule
import time
import datetime

def CreateFile():
    timeStamp = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

    FileName = "File_"+timeStamp+".txt"

    CreationDate = datetime.datetime.now().strftime("%d-%m-%Y")
    CreationTime = datetime.datetime.now().strftime("%I:%M:%S %p")

    fobj = open(FileName,"w")
    fobj.write("Filename: "+FileName+"\n")
    fobj.write("Creation date: "+CreationDate+"\n")
    fobj.write("Creation time: "+CreationTime+"\n")
    fobj.close()

    print("File Gets Created With Name :",FileName)

def main():
    print("Automation Script Started")

    schedule.every(1).minute.do(CreateFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()
