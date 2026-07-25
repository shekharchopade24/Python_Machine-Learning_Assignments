import schedule
import time
import datetime

def display():
    timeStamp = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    fobj = open("Marvellous.txt","a")
    fobj.write("Task executed at: "+timeStamp+"\n")
    fobj.close()

def main():
    print("Automation Script Started")

    schedule.every(5).minutes.do(display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()
