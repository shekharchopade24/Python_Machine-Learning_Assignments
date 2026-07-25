import schedule
import time
import datetime

def CreateLogFile():
    timeStamp = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

    LogFileName = "MarvellousLog_"+timeStamp+".txt"

    DisplayTime = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    fobj = open(LogFileName,"w")
    fobj.write("Log file created successfully.\n")
    fobj.write("Creation Time: "+DisplayTime+"\n")
    fobj.close()

    print("Log file Gets Created With Name :",LogFileName)

def main():
    print("Automation Script Started")

    schedule.every(10).minutes.do(CreateLogFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()
