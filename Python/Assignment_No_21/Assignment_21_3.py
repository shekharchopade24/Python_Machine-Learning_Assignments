import threading

Counter = 0
Lock = threading.Lock()

def UpdateCounter():
    global Counter

    for i in range(100000):
        Lock.acquire()
        Counter = Counter + 1
        Lock.release()

def main():
    t1 = threading.Thread(target=UpdateCounter)
    t2 = threading.Thread(target=UpdateCounter)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Final value of Counter :", Counter)

if __name__ == "__main__":
    main()