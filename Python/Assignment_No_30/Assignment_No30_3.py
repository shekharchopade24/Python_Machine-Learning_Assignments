import schedule
import time

def display():
    print("Coding Kar..!")

def main():
    print("Automation Script Started")

    schedule.every(30).minutes.do(display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()
