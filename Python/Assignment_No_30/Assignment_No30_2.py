import schedule
import time
import datetime

def display():
    timeStamp = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
    print("Current Date and Time:",timeStamp)

def main():
    print("Automation Script Started")

    schedule.every(1).minute.do(display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()
