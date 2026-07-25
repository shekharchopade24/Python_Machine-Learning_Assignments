import sys
import os
import time
import schedule
import MarvellousDuplicateModule as MM

sender_email = "python.test@gmail.com"

app_password = "xxxx xxxx xxxx xxxx"

def DisplayHelp():
    print("Duplicate File Removal Automation")
    print()
    print("This script scans a directory, identifies duplicate files using checksums,")
    print("deletes duplicate files, creates a log file, and sends the log file through email.")
    print()
    print("Usage:")
    print("    python DuplicateFileRemoval.py <DirectoryPath> <IntervalInMinutes> <ReceiverEmail>")
    print()
    print("Example:")
    print("    python DuplicateFileRemoval.py E:/Data/Demo 50 marvellousinfosystem@gmail.com")

def DisplayUsage():
    print("Usage:")
    print("python DuplicateFileRemoval.py <AbsoluteDirectoryPath> <TimeIntervalInMinutes> <ReceiverEmailAddress>")

def ValidateDirectory(DirectoryPath):
    Ret = os.path.isabs(DirectoryPath)
    if(Ret == False):
        print("Marvellous Automation Error : Directory Path Should Be Absolute")
        return False

    Ret = os.path.exists(DirectoryPath)
    if(Ret == False):
        print("Marvellous Automation Error : There Is No Such Directory With Name",DirectoryPath)
        return False

    Ret = os.path.isdir(DirectoryPath)
    if(Ret == False):
        print("Marvellous Automation Error : Given Path Is Not A Directory",DirectoryPath)
        return False

    Ret = os.access(DirectoryPath,os.R_OK)
    if(Ret == False):
        print("Marvellous Automation Error : Permission Denied For Directory",DirectoryPath)
        return False

    return True

def ValidateInterval(Interval):
    Ret = Interval.isdigit()
    if(Ret == False):
        print("Marvellous Automation Error : Interval Should Be Numeric")
        return False

    if(int(Interval) <= 0):
        print("Marvellous Automation Error : Interval Should Be Greater Than Zero")
        return False

    return True

def ValidateEmail(EmailAddress):
    if("@" in EmailAddress and "." in EmailAddress):
        return True
    else:
        print("Marvellous Automation Error : Invalid Email Address",EmailAddress)
        return False

def PerformDuplicateRemoval(DirectoryPath,ReceiverEmail):
    LogDirectory = MM.CreateLogDirectory("Marvellous")
    LogFilePath = MM.CreateLogFile(LogDirectory)

    Stats = MM.RemoveDuplicateFiles(DirectoryPath,LogFilePath)

    Subject = "Duplicate File Removal Report"

    Body = "Jay Ganesh,\n\n"
    Body = Body+"The duplicate-file removal operation has been completed successfully.\n\n"
    Body = Body+"Operation Statistics:\n\n"
    Body = Body+"Starting time of scanning: "+Stats["StartTime"]+"\n"
    Body = Body+"Completion time of scanning: "+Stats["EndTime"]+"\n"
    Body = Body+"Directory scanned: "+DirectoryPath+"\n"
    Body = Body+"Total number of files scanned: "+str(Stats["TotalFiles"])+"\n"
    Body = Body+"Total number of duplicate files found: "+str(Stats["DuplicateFound"])+"\n"
    Body = Body+"Total number of duplicate files deleted: "+str(Stats["DuplicateDeleted"])+"\n\n"
    Body = Body+"Please find the detailed log file attached to this email.\n\n"
    Body = Body+"Regards,\nMarvellous Automation System"

    MM.Marvellous_send_mail(sender_email,app_password,ReceiverEmail,Subject,Body,LogFilePath,LogFilePath)

def main():
    Border = "-"*40

    if(len(sys.argv)==2):
        if(sys.argv[1]=="--help" or sys.argv[1]=="-h"):
            DisplayHelp()

        elif(sys.argv[1]=="--usage" or sys.argv[1]=="-u"):
            DisplayUsage()

        else:
            print("Marvellous Automation Error : Invalid Option",sys.argv[1])
            print("Plss use '--help' or '--usage' for more Info")

    elif(len(sys.argv)==4):
        DirectoryPath = sys.argv[1]
        Interval = sys.argv[2]
        ReceiverEmail = sys.argv[3]

        Ret1 = ValidateDirectory(DirectoryPath)
        Ret2 = ValidateInterval(Interval)
        Ret3 = ValidateEmail(ReceiverEmail)

        if(Ret1 == True and Ret2 == True and Ret3 == True):
            IntervalInMinutes = int(Interval)

            print(Border)
            print("Marvellous Automation Script Started")
            print(Border)

            schedule.every(IntervalInMinutes).minutes.do(PerformDuplicateRemoval,DirectoryPath,ReceiverEmail)

            while True:
                schedule.run_pending()
                time.sleep(1)
        else:
            print("Marvellous Automation Error : Invalid Input Parameters")

    else:
        print("Invalid number of arguments")
        print("Plss use '--help' or '--usage' for more Info")

if __name__=="__main__":
    main()
