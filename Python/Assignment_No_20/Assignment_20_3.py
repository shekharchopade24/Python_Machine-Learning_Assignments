import threading
from functools import reduce
Ret = lambda x :x if x % 2 == 0 else False
Ret1 = lambda x : x if x % 2 !=0 else False
Add = lambda x,y :x+y

def GetEven(Value):
    Data2 = list(filter(Ret, Value))
    Result = reduce(Add,Data2)
    print("Even Data :",Data2)
    print("Even Sum :",Result)
   
  


def GetOdd(Value):
    Data2 = list(filter(Ret1, Value))
    Result = reduce(Add,Data2)
    print("Odd Data :",Data2)
    print("Odd Sum :",Result)
   
        


def main():
    Data=[2,1,22,20,11,90,80,6,7,3,2,1]
    EvenFactor = threading.Thread(target=GetEven, args=(Data,))
    EvenFactor.start()
    
    
    OddFactor = threading.Thread(target=GetOdd, args= (Data,))
    OddFactor.start()

    print("Exit From Main")
    

if __name__=="__main__":
    main()