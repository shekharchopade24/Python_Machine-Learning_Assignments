import os
import hashlib
import datetime
import smtplib
from email.message import EmailMessage

def CalculateCheckSum(FileName):
    try:
        fobj = open(FileName,"rb")

        hobj = hashlib.md5()

        Buffer = fobj.read(1024)

        while(len(Buffer) > 0):
            hobj.update(Buffer)
            Buffer = fobj.read(1024)

        fobj.close()
        return hobj.hexdigest()
    except Exception as fobj1:
        return None

def CreateLogDirectory(LogDirectory):
    Ret = os.path.exists(LogDirectory)

    if(Ret == False):
        os.mkdir(LogDirectory)

    return LogDirectory

def CreateLogFile(LogDirectory):
    timeStamp = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

    LogFileName = "DuplicateRemovalLog_"+timeStamp+".log"

    LogFilePath = os.path.join(LogDirectory,LogFileName)

    return LogFilePath

def WriteLog(LogFilePath,Message):
    fobj = open(LogFilePath,"a")
    fobj.write(Message+"\n")
    fobj.close()

def RemoveDuplicateFiles(DirectoryPath,LogFilePath):
    StartTime = datetime.datetime.now().strftime("%d %B %Y, %I:%M:%S %p")

    WriteLog(LogFilePath,"Starting time of scanning: "+StartTime)
    WriteLog(LogFilePath,"Directory scanned: "+DirectoryPath)

    CheckSumDict = {}

    TotalFiles = 0
    DuplicateFound = 0
    DuplicateDeleted = 0

    for FolderName , SubFolder , FileName in os.walk(DirectoryPath):
        for fname in FileName:
            FilePath = os.path.join(FolderName,fname)

            Ret = os.path.isfile(FilePath)
            if(Ret == False):
                continue

            TotalFiles = TotalFiles + 1

            CheckSumValue = CalculateCheckSum(FilePath)

            if(CheckSumValue is None):
                WriteLog(LogFilePath,"Unable to read file : "+FilePath)
                continue

            if(CheckSumValue in CheckSumDict):
                DuplicateFound = DuplicateFound + 1

                WriteLog(LogFilePath,"Duplicate File Found : "+FilePath+" CheckSum : "+CheckSumValue)

                try:
                    os.remove(FilePath)
                    DuplicateDeleted = DuplicateDeleted + 1
                    WriteLog(LogFilePath,"Deleted Duplicate File : "+FilePath)
                except PermissionError as fobj1:
                    WriteLog(LogFilePath,"Permission Denied For File : "+FilePath+" "+str(fobj1))
                except Exception as fobj2:
                    WriteLog(LogFilePath,"Unable To Delete File : "+FilePath+" "+str(fobj2))
            else:
                CheckSumDict[CheckSumValue] = FilePath

    EndTime = datetime.datetime.now().strftime("%d %B %Y, %I:%M:%S %p")

    WriteLog(LogFilePath,"Completion time of scanning: "+EndTime)
    WriteLog(LogFilePath,"Total number of files scanned: "+str(TotalFiles))
    WriteLog(LogFilePath,"Total number of duplicate files found: "+str(DuplicateFound))
    WriteLog(LogFilePath,"Total number of duplicate files deleted: "+str(DuplicateDeleted))

    Stats = {}
    Stats["StartTime"] = StartTime
    Stats["EndTime"] = EndTime
    Stats["TotalFiles"] = TotalFiles
    Stats["DuplicateFound"] = DuplicateFound
    Stats["DuplicateDeleted"] = DuplicateDeleted

    return Stats

def Marvellous_send_mail(sender,app_password,receiver,subject,body,AttachmentPath,LogFilePath):
    try:
        msg = EmailMessage()

        msg["From"] = sender
        msg["To"] = receiver
        msg["Subject"] = subject

        msg.set_content(body)

        if(os.path.exists(AttachmentPath)):
            fobj = open(AttachmentPath,"rb")
            FileData = fobj.read()
            FileName = os.path.basename(AttachmentPath)
            fobj.close()

            msg.add_attachment(FileData,maintype="application",subtype="octet-stream",filename=FileName)

        smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)

        smtp.login(sender,app_password)

        smtp.send_message(msg)

        smtp.quit()

        WriteLog(LogFilePath,"Email delivery status: Success")
        return True
    except Exception as fobj1:
        WriteLog(LogFilePath,"Email delivery status: Failure -- "+str(fobj1))
        return False
