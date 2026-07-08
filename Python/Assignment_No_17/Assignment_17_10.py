
def Ret(No):
    sum = 0
    while(No !=0):
        No1 = No % 10
        sum = sum+No1
        No = No //10

    return sum


def main():
    Value = int(input("Enter Value :"))
    Result = Ret(Value)
    print("Count :",Result)
    

if __name__ == "__main__":
    main()