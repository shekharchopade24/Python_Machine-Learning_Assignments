import schedule
import time

def LunchTime():
    print("Lunch Time!")

def WrapUpWork():
    print("Wrap up work")

def main():
    print("Automation Script Started")

    schedule.every().day.at("13:00").do(LunchTime)
    schedule.every().day.at("18:00").do(WrapUpWork)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()
