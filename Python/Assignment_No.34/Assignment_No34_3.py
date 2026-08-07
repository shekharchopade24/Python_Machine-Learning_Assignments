import sys
import schedule
from AModule_ProcInfoLog import PlatformSurvillence

def main():
    Border = "-"*50
    print(Border)
    print("---Marvellous Platform Survillence System---")
    print(Border)

    FolderName = sys.argv[1]
    PlatformSurvillence(FolderName)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Automation Script is use to Perform")
            print("1: It fetch the information of Running Process")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the Automation Script as :")
            print(f"python {sys.argv[0]} Folder_Name")
            print("Folder_Name : Name of Folder for the log file storage")

        else:
            print("Unable to proceed as arguments are not matching argumnets")
            print("Please use --h and --u flag for getting more details")
            

    # Actual code
    elif(len(sys.argv) == 3):
        
        # print("CPU Usage :",psutil.cpu_percent())
        print("Schedular Started Successfuly")
        print("Press ctrl+c to Abort the Automation Script")

    else:
        print("Invalid Number of Arguments")
        print("Unable to proceed as arguments are not matching argumnets")
        print("Please use --h and --u flag for getting more details")

    print(Border)
    print("Thank For Using our Automation System")
    print(Border)

if __name__ == "__main__":
    main()