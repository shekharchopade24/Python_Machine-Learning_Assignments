import psutil
import os
import time


def ProcessScan():
    ListInfo = []
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs = ["pid","name","status"])
        if info["status"] == "running":
            ListInfo.append(info)
    return ListInfo

def PlatformSurvillence(FolderName):
    Border = "-"*50
    Ret = False

    Ret = os.path.exists(FolderName)
    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to Proceed As folder name is Existing but it is not a directory")
            return
    else:
        os.mkdir(FolderName)
        print(f"Directory for the log file created Successfullly names As {FolderName}")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName,"Marvellous_%s.log" %timestamp)

    fobj = open(FileName,"w")

    print(f"Log file gets Successfullly Created with Name {FileName}")

    fobj.write(Border+"\n")
    fobj.write("---Marvellous Platform Survillence System---\n")
    fobj.write("Log file gets created At :"+timestamp+"\n")
    fobj.write(Border+"\n\n")

    fobj.write("-----------------------System Report---------------------------\n")

    Data = ProcessScan()

    for info in Data:
        fobj.write("PID: %s\n" %info.get("pid"))
        fobj.write("Name: %s\n" %info.get("name"))
        fobj.write("Status: %s\n" %info.get("status"))
        fobj.write(Border+"\n\n")

    fobj.write(Border+"\n\n")
    fobj.write("-----------------------End of Log File---------------------------")
    fobj.write(Border+"\n\n")

    fobj.close()
