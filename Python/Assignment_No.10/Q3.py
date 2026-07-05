def NaturalNumber(No):
    Ans = 1
    for i in range(1 ,No+1):
        Ans = Ans * i
    return Ans


def main():
    iValue = int(input("Enter Number to get Factorial :"))
    Ret = 0

    Ret = NaturalNumber(iValue)
    
    print(Ret)
    
if __name__  == "__main__":
    main()