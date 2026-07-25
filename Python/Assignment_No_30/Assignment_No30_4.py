import schedule
import time

def display():
    print("Namskar...")

def main():
    print("Automation Script Started")

    schedule.every().day.at("09:00").do(display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()
