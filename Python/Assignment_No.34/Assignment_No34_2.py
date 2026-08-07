import sys
import schedule
import time 
from AModule_ProcInfo import ProcessScan1

def main():
    Border = "-"*50
    print(Border)
    print("---Marvellous Platform Survillence System---")
    print(Border)
    ProcName = sys.argv[1]
    ProcessScan1(ProcName)
     
    print(Border)
    print("Thank For Using our Automation System")
    print(Border)

if __name__ == "__main__":
    main()