import threading

def GetEven(No):
    sum = 0
    for i in range(1,No):
        if No % i==0:
           sum=sum+i
    print("Even Factor sum",sum)



def GetOdd(No):
    sum = 0
    for i in range(1,No):
        if No % i==0:
           sum=sum+i
    print("Odd Factor Sum",sum)

        


def main():
    
    EvenFactor = threading.Thread(target=GetEven, args=(20,))
    EvenFactor.start()
    
    
    OddFactor = threading.Thread(target=GetOdd, args= (21,))
    OddFactor.start()

    print("Exit From Main")
    

if __name__=="__main__":
    main()