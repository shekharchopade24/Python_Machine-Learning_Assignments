import sys
import schedule
import time
from AModule_ProcInfoLog2 import PlatformSurvillence

def main():
    Border = "-"*50
    print(Border)
    print("---Marvellous Platform Survillence System---")
    print(Border)
    
    # --h and --u handling
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Automation Script is use to Perform")
            print("1: It fetch the information of Running Process")
            print("2: It fetch the information about prmmary storage as RAM")
            print("3: It fetch the information about secondary storage as HDD")
            print("4: It fetch the information about Microprocessor")
            print("5: It gets auto scheduled periodically")
            print("6: It Manitans all record into log file")
            print("7: It sends log files through mail periodically")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the Automation Script as :")
            print(f"python {sys.argv[0]} Time_interval Folder_Name Receiver_Email")
            print("Time_interval : Time in minutes for periodic execution")
            print("Folder_Name : Name of Folder for the log file storage")
            print("Receiver_Email : Email Address to send the log file ")

        else:
            print("Unable to proceed as arguments are not matching argumnets")
            print("Please use --h and --u flag for getting more details")
            
    elif(len(sys.argv) == 4):
        print("Press ctrl+c to Abort the Automation Script")
        schedule.every(int(sys.argv[1])).minutes.do(PlatformSurvillence, sys.argv[2],sys.argv[3])

        try:
            while True:
                schedule.run_pending()
                time.sleep(1)

        except KeyboardInterrupt:
            print("\n"+Border)
            print(f"Automation Script Stopped Successfully by User")
            print(Border)
        
    else:
        print("Invalid Number of Arguments")
        print("Unable to proceed as arguments are not matching argumnets")
        print("Please use --h and --u flag for getting more details")

    print(Border)
    print("Thank For Using our Automation System")
    print(Border)

if __name__ == "__main__":
    main()