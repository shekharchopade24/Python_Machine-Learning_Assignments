import threading

def GetEven():
    for i in range(2,21,2):
        print(i, end=" ")
    print()

def GetOdd():
    for i in range(1,21,2):
        print(i, end=" ")
    print()
    
def main():
    print("Even")
    Even = threading.Thread(target=GetEven)
    Even.start()
    print("Odd")
    Odd = threading.Thread(target=GetOdd)
    Odd.start()

if __name__=="__main__":
    main()