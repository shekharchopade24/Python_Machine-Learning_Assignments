
def Ret(No):
    cnt = 0
    while(No !=0):
        No1 = No % 10
        cnt = cnt+1
        No = No //10

    return cnt


def main():
    Value = int(input("Enter Value :"))
    Result = Ret(Value)
    print("Count :",Result)
    

if __name__ == "__main__":
    main()