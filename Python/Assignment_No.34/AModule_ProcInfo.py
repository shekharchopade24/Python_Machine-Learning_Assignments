import psutil
import os

def ProcessScan():
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs = ["pid","name","username","status"])
        if(info["status"] == "running"):
            print("-------------------------------------------")
            print(info)
            print("-------------------------------------------")


def ProcessScan1(ProcName):
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs = ["pid","name","username","status"])
        if(info["status"] == "running"  and info["name"] == ProcName):
            print("-------------------------------------------")
            print(info)
            print("-------------------------------------------")
        
