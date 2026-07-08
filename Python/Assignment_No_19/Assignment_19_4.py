
from functools import reduce
Filt =lambda x :x if x % 2 ==0  else False
Ret2 = lambda x : x*x
Ret3 = lambda x ,y: (x+y)

def main():
    No = int(input("Enter How many Elements :"))
    Data = []
    for i in range(1,No+1):
        Value = int(input("Enter Data :"))
        Data.append(Value)

    print(Data)
    Result = list(filter(Filt,Data))
    print(Result)

    Result2 = list(map(Ret2,Result))
    print(Result2)

    Result3 = reduce(Ret3,Result2)
    print("Product Of THe FInal List :",Result3)

if __name__=="__main__":
    main()