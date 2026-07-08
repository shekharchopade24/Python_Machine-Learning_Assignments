
from functools import reduce

Ret2 = lambda x : x*2
Ret3 = lambda x ,y: x if x>y  else y 

def PrimeNO(No):
    Flg = True
    for i in range(2,int(No/2)+1):
        if No % i == 0 :

            Flg = False
            break
        else:
            Flg = True

    return Flg

def main():
    No = int(input("Enter How many Elements :"))
    Data = []
    for i in range(1,No+1):
        Value = int(input("Enter Data :"))
        Data.append(Value)

    print(Data)
    Result = list(filter(PrimeNO,Data))
    print(Result)

    Result2 = list(map(Ret2,Result))
    print(Result2)

    Result3 = reduce(Ret3,Result2)
    print("Maximum Of THe FInal List :",Result3)

if __name__=="__main__":
    main()